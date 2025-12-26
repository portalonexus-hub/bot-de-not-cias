import os
import feedparser
import tweepy

auth = tweepy.OAuth1UserHandler(
    os.environ["API_KEY"],
    os.environ["API_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_SECRET"
)

api = tweepy.API(auth)

rss = "https://g1.globo.com/rss/g1/"
feed = feedparser.parse(rss)

noticia = feed.entries[0]
tweet = noticia.title + "\n" + noticia.link

api.update_status(tweet)
