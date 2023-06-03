import twitter
import sys


def connect_twitter_account(credential_file):
    (CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = (
        open(credential_file, "r").read().splitlines()
    )

    auth = twitter.oauth.OAuth(
        OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
    )
    return twitter.Twitter(auth=auth)


def get_account_info(twitter_obj):
    if twitter_obj is not None:
        query = twitter_obj.search.tweets(
            q="#python",
            lang="en",
            count="10",
        )["statuses"]

        for q in query:
            for key, value in q.items():
                if key == "text":
                    print(f"{value}\n")


def main():
    try:
        twitter_obj = connect_twitter_account("credentials.txt")
        get_account_info(twitter_obj)

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
    sys.exit(1)
