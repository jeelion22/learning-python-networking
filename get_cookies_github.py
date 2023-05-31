import requests


def check_httponly(c):
    if "httponly" in c._rest.keys():
        return True
    else:
        return "\x1b[31mFalse\x1b[39;49m"


cookies = []

url = "http://www.github.com"

response = requests.get(url)

for cookie in response.cookies:
    print(f"Name: {cookie.name}\nValue: {cookie.value}")
    cookies.append(cookie.value)

    if not cookie.secure:
        cookie.secure = "'\x1b[31mFalse\x1b[39;49m'"
    print("HTTPOnly:", check_httponly(cookie), "\n")

print(set(cookies))
