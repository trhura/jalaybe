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
last_synced_time = datetime.now()

@app.route('/')
def hello():
    outstr = ""
    outstr += "<h3> Schedule </h3>"
    outstr += "&nbsp;&nbsp;&nbsp;&nbsp;current time: " + datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    outstr += "</br>&nbsp;&nbsp;&nbsp;&nbsp;last synced time: " + last_synced_time.strftime("%A, %d. %B %Y %I:%M%p")

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
            get_postid = lambda x: int(x['id'].split('_')[1])

            thispage = config['pages'][pageid]
            sourcepage = str(thispage['from'])
            arguments = {'limit': 5, 'fields': 'link,name,picture,description,message'}
            response = graph.get_connections(sourcepage, 'feed', **arguments)

            total_posts = 0
            posts = response['data']
            lastpostid = get_postid(posts[0])
            posts.reverse()

            # For first run, just save the last postid skip posting
            if thispage['last_synced_post'] != 0:
                for post in posts:
                    if get_postid(post) <= thispage['last_synced_post']:
                        continue

                    # if postid is newer than last sycned share it
                    message = converter.zg12uni51(post['message'])
                    message = message.encode('utf8')

                    del post['id']
                    del post['message']
                    total_posts += 1
                    if post.has_key('description'):
                        post['description'] = post['description'].encode('utf8')

                    graph.put_wall_post(message=message, attachment=post)

            logging.info ("Synced %d posts for %s." %(total_posts, thispage['name']))
            thispage['last_synced_post'] = lastpostid

    last_synced_time = datetime.now()
    return 'ok', 200

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
