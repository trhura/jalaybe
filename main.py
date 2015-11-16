"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
import yaml
import pytz
import facebook
import logging
import converter
from datetime import datetime
from flask import Flask

def get_config(yamlfile):
    with open(yamlfile, 'r') as stream:
        obj = yaml.load(stream)
        return obj

app = Flask(__name__)
config = get_config('config.yaml')
recent_synced_time = datetime.now()

@app.route('/')
def hello():
    outstr = ""
    outstr += "<h3> Schedule </h3>"
    outstr += "&nbsp;&nbsp;&nbsp;&nbsp;current time: " + datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    outstr += "</br>&nbsp;&nbsp;&nbsp;&nbsp;last synced time: " + recent_synced_time.strftime("%A, %d. %B %Y %I:%M%p")

    outstr += "<h3> Pages </h3>"
    for page, details  in config['pages'].items():
        outstr += '&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.facebook.com/%s">%s</a>' %(page, details['name'])
        outstr += ' (last synced: <a href="http://www.facebook.com/%s/posts/%s">%s</a>)' \
                  %(details['from'], details['last_synced_post'], details['last_synced_post'])
        outstr += "<br/>"

    return outstr

@app.route('/sync')
def sync():
    graph = facebook.GraphAPI(config['user_access_token'])
    resp = graph.get_object('me/accounts')

    # For each page that the user manage
    for page in resp['data']:
        pageid = int(page['id'])

        # if the page is configured to sync
        if config['pages'].has_key(pageid):
            page_access_token = page['access_token']
            graph = facebook.GraphAPI(page_access_token)
            getpostid = lambda x: int(x['id'].split('_')[1])
            gettime = lambda x: datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')

            thispage = config['pages'][pageid]
            sourcepage = str(thispage['from'])
            arguments = {'limit': 2, 'fields': 'link,name,picture,description,message,created_time'}
            response = graph.get_connections(sourcepage, 'feed', **arguments)

            total_posts = 0
            posts = response['data']
            last_synced_time = posts[0]['created_time']
            last_synced_post = getpostid(posts[0])
            posts.reverse()

            # First run, get the last post time from destination page
            if thispage['last_synced_time'] == 0:
                arguments = {'limit': 1, 'fields': 'created_time'}
                response = graph.get_connections(page['id'], 'feed', **arguments)
                thispage['last_synced_time'] = response['data'][0]['created_time']

            for post in posts:
                if gettime(post['created_time']) <= gettime(thispage['last_synced_time']):
                    continue

                # if postid is newer than last sycned share it
                message = None
                if post.has_key('message'):
                    message = converter.zg12uni51(post['message']).encode('utf8')

                if post.has_key('description'):
                    post['description'] = converter.zg12uni51(post['description']).encode('utf8')

                if not post.has_key('link'):
                    post['link'] = 'https://www.facebook.com/%s/posts/%s' %(pageid, getpostid(post))

                if post.has_key('name'):
                    post['name'] = converter.zg12uni51(post['name']).encode('utf8')
                else:
                    post['name'] = thispage['name']

                del post['id']
                total_posts += 1
                if post.has_key('message'): del post['message']
                graph.put_wall_post(message=message, attachment=post)

            logging.info ("Synced %d posts for %s." %(total_posts, thispage['name']))
            thispage['last_synced_post'] = last_synced_post
            thispage['last_synced_time'] = last_synced_time

    global recent_synced_time
    recent_synced_time = datetime.now()
    return 'ok', 200

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
