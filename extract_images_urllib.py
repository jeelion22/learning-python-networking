from urllib.request import urlopen, urljoin
from html.parser import HTMLParser
import re


# fucntion for getting response object
def download_page(url):
    return urlopen(url).read().decode("utf-8")


# fucntion for extracting images
def extract_image_location(page):
    img_regex = re.compile(r'<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return img_regex.findall(page)


if __name__ == "__main__":
    target_url = "https://www.google.com"

    pages = download_page(target_url)

    image_locations = extract_image_location(pages)

    for src in image_locations:
        print(urljoin(target_url, src))
