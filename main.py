
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

from requests_toolbelt.adapters import appengine
appengine.monkeypatch()

app = Flask(__name__)
config = get_config('config.yaml')
recent_synced_time = 0

@app.route('/')
def hello():
    nbsp = '&nbsp;&nbsp;&nbsp;&nbsp;'
    outstr = ""
    outstr += "<h3> Schedule </h3>"
    outstr += nbsp + "current time: " + datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    outstr += nbsp + "</br>&nbsp;&nbsp;&nbsp;&nbsp;last synced time: " + str(recent_synced_time)

    outstr += "<h3> Pages </h3>"
    for page in config['pages']:
        outstr += '&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.facebook.com/%s">%s</a>' %(page, page['name'])
        outstr += '(last synced: <a href="http://www.facebook.com/%s/posts/%s">%s</a>)' \
                   %(page['from'], page['last_synced_post'], page['last_synced_post'])
        outstr += "<br/>"

    return outstr

@app.route('/sync')
def sync():
    global recent_synced_time
    destpageID = config['destpage']
    graph = facebook.GraphAPI(config['access_token'])
    getpostid = lambda x: int(x['id'].split('_')[1])
    gettime = lambda x: datetime.strptime(x[:-5], '%Y-%m-%dT%H:%M:%S')

    for page in config['pages']:
        sourcepage = page['from']
        arguments = {'limit': 2, 'fields': 'link,name,picture,description,message,created_time'}
        response = graph.get_connections(sourcepage, 'feed', **arguments)

        total_posts = 0
        posts = response['data']
        last_synced_time = posts[0]['created_time']
        last_synced_post = getpostid(posts[0])
        posts.reverse()

        # First run, get the last post time from destination page
        if recent_synced_time == 0:
            arguments = {'limit': 1, 'fields': 'created_time'}
            response = graph.get_connections(destpageID, 'feed', **arguments)
            recent_synced_time = gettime(response['data'][0]['created_time'])

        for post in posts:
            if gettime(post['created_time']) <= recent_synced_time:
                continue

            # if postid is newer than last sycned share it
            message = ''
            if post.has_key('message'):
                message = converter.zg12uni51(post['message']).encode('utf8')

            if post.has_key('description'):
                post['description'] = converter.zg12uni51(post['description']).encode('utf8')

            if not post.has_key('link'):
                post['link'] = 'https://www.facebook.com/%s/posts/%s' %(destpageID, getpostid(post))

            if post.has_key('name'):
                post['name'] = converter.zg12uni51(post['name']).encode('utf8')
            else:
                post['name'] = page['name']

            thepost = post
            total_posts += 1
            del thepost['id']
            if thepost.has_key('message'): del thepost['message']
            graph.put_wall_post(message=message, attachment=post)

            logging.info ("Synced %d posts for %s." %(total_posts, page['name']))
            page['last_synced_post'] = last_synced_post
            page['last_synced_time'] = last_synced_time

    recent_synced_time = datetime.now()
    return 'ok', 200

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    return 'Sorry, unexpected error: {}'.format(e), 500
