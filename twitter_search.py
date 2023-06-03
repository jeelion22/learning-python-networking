import json, twitter


def connect_twitter_account(credential_file):
    CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = (
        open(credential_file, "r").read().splitlines()
    )
    auth = twitter.oauth.OAuth(
        CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
    )
    print("connection checked")
    return twitter.Twitter(auth=auth)


def get_recent_tweets(twitter_obj, search_term):
    search = twitter_obj.search.tweets(q=search_term, lang="en", count="10")["statuses"]
    print(search)
    return search


def save_tweets(tweets, file):
    with open(file, "w") as f:
        json.dumps(tweets, f, indent=1)


def main():
    try:
        search_item = input("Enter the search term in twitter: ")
        tw = connect_twitter_account("credentials.txt")
        tweets = get_recent_tweets(tw, search_item)
        save_tweets(tweets, "recent_tweets.txt")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
