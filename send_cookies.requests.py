import requests

cookies = []

url = "http://httpbin.org/cookies"

cookies = dict(admin="True", login="False")

print("My cookies: ", cookies)

cookie_req = requests.get(url, cookies=cookies)

print(cookie_req.text)
