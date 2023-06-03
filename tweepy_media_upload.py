import tweepy
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_key = config["twitter"]["api_key"]
api_key_secret = config["twitter"]["api_key_secret"]
access_token = config["twitter"]["access_token"]
access_token_secret = config["twitter"]["access_token"]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


filename = "self_control.jpg"
status = "Be Motivated, updated with tweepy"

print("media to be uploaded:", filename)
print("status for the media is: ", status)

print("media is being uploaded...")
api.update_status_with_media(status, filename)

print("upload done.")
# consumer_key = api_key
# consumer_secret = api_key_secret
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# # set access to user's access key and access secret
# auth.set_access_token(access_token, access_token_secret)

# # calling the api
# api = tweepy.API(auth)

# # the text to be tweeted
# status = "This is a media upload."

# # the path of the media to be uploaded
# filename = "self_control.jpg"

# # posting the tweet
# api.update_status_with_media(status, filename)
