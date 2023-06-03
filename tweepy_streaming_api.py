import tweepy
import json
from time import sleep


def twitter_connection(file):
    CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = (
        open(file, "r").read().splitlines()
    )

    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return (tweepy.API(auth), auth)


class StreamListener(tweepy.StreamListener):
    def on_data(self, data):
        data = json.loads(data)
        print(data)
        return True

    def on_limit(self, track):
        print(f"[!] Limit: {track}")
        sleep(10)


def on_error(self, status):
    print("[!] Error: {0}".format(status))
    return False


def get_trending_topics(woeid=1):
    trends = api.tends_place()
