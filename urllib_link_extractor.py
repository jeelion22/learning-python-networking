from urllib.request import urlopen
import re


def download_page(url):
    return urlopen(url).read().decode("utf-8")


def extract_link(page):
    link_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # link_regex = re.compile(r"<p>(.*?)</p>")
    return link_regex.findall(page)


if __name__ == "__main__":
    url = "https://www.python.org"

    page = download_page(url)
    links = extract_link(page)

    for link in links:
        print(link)
