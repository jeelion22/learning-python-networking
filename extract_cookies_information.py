import http.cookiejar
import urllib.request

url = "https://github.com/"


def extract_cookie_info():
    cookie_jar = http.cookiejar.CookieJar()
    cookie_processor = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(cookie_processor)
    urllib.request.install_opener(opener)

    response = opener.open(url)

    for cookie in cookie_jar:
        print(f"Cookie: {cookie.name} --> {cookie.value}")
    print(f"Headers: {response.headers}")


if __name__ == "__main__":
    extract_cookie_info()
