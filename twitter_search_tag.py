import requests, requests_oauthlib, sys, json
from urllib.parse import urlparse


def init_auth(file):
    CONSUMER_KEY, CONUSMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET = (
        open(file, "r").read().splitlines()
    )

    auth_obj = requests_oauthlib.OAuth1(
        CONSUMER_KEY, CONUSMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
    )
    if verify_credentials(auth_obj):
        print("Validated Credntials OK")
    else:
        print("Credntial validation failed")
        sys.exit(1)


def verify_credentials(auth_obj):
    url = "https://api.twitter.com/1.1/account/verify_credentials.json"
    response = requests.get(url, auth=auth_obj)

    for key, value in json.loads(response.text).items():
        print(f"{key}: {value}")

    return response.status_code == 200


def get_mentions(since_id, auth_obj):
    params = {
        "count": 200,
        "since_id": since_id,
        "include_rts": 0,
        "include_entities": "false",
    }
    url = "https://api.twitter.com/1.1/statuses/mentions_timeline.json"
    response = requests.get(url, params=params, auth=auth_obj)

    print(f"Response Status: {response.status_code}")
    # print(urlparse(url))

    response.raise_for_status()
    return json.loads(response.text)


def search(auth_obj):
    params = {"query": "python"}
    url = "https://api.twitter.com/2/tweets/search/all"
    response = requests.get(url, params=params, auth=auth_obj)
    print(f"search response: {response.status_code}")
    return response


if __name__ == "__main__":
    auth_obj = init_auth("credentials.txt")
    since_id = 1
    response = search(auth_obj)
    print(json.dumps(response.json(), indent=2))
