import requests

from requests.auth import HTTPDigestAuth

url = "https://httpbin.org/digest-auth/auth/user/passwd"

response = requests.get(url, auth=HTTPDigestAuth("user", "passwd"))


if response.status_code == 200:
    print(f"Login sucessful: {response.json()}")
