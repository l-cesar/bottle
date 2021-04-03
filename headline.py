#!/usr/bin/python3
import feedparser
from flask import Flask
app = Flask(__name__)

bbc_feed = "http://feeds.bbci.co.uk/news/rss.xml"


@app.route('/')
def get_news():
    feed = feedparser.parse(bbc_feed)
    first_article = feed['entries']
    return 'lorem ipsum dolor sit amet'

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
   and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)

