import tweepy
import configparser
import pandas as pd
import os

# script for saving home_timeline as a csv file

# credentials configuration
config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["twitter"]["api_key"]
api_key_secret = config["twitter"]["api_key_secret"]
access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token_secret"]

# authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()

# prints all tweets
print(public_tweets)

data = []

# saving public_tweets attributes as a csv file using pandas
columns = ["Time", "User", "Tweet"]

for tweet in public_tweets:
    data.append([tweet.created_at, tweet.user_screen_name, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_excel("twwets.csv")
