from html.parser import HTMLParser
import urllib.request


# extracts all linkes related to http/s protocols
class GetLinks(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            # print(attrs)
            for a in attrs:
                if a[0] == "href":
                    link = a[1]
                    if link.find("http") >= 0:
                        print(link)
                        new_parser = GetLinks()
                        # gets links from the link
                        new_parser.feed(link)


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Black-and-yellow_broadbill"
    req = urllib.request.urlopen(url)
    parser = GetLinks()
    parser.feed(req.read().decode("utf-8"))
