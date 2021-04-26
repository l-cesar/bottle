#!/usr/bin/python3

import feedparser
from flask import Flask
app = Flask(__name__)

bbc_feed = "http://feeds.bbci.co.uk/news/rss.xml"

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
	feed = feedparser.parse(RSS_FEEDS[publication])
	first_article = feed['entries'][0]
	render_template("home.html", title=first_article.get("title"), published=first_article.get("published"), summary=first_article.get("summary"))

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

