import os
import requests
from lxml import html


class Scraping:
    def scrapingImages(self, url):
        print(f"getting images from {url}")

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            # path expression for getting images
            images = parsed_body.xpath("//img/@src")

            print(f"found images {len(images)}.")

            # create a directory for save images

            os.system("mkdir images")

            for image in images:
                if image.startswith("http") == False:
                    download = url + "/" + image

                else:
                    download = image

                print(download)

                r = requests.get(download)
                f = open("images/%s" % download.split("/")[-1], "wb")
                f.write(r.content)
                f.close()

        except Exception as e:
            print(f"Connection error in {url}")
            pass

    def scrapingLinks(self, url):
        print(f"\nGetting links from url: {url}")

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)
            links = parsed_body.xpath("//a/@href")
            print(f"Found links {len(links)}")

            for link in links:
                print(link)

        except Exception as e:
            print(f"Connection error in {url}.")


if __name__ == "__main__":
    target = "https://www.amazon.in/s?k=DSA+in+python&crid=1AVPMAXKLOJMF&sprefix=dsa+in+python%2Caps%2C326&ref=nb_sb_noss_1"
    scraping = Scraping()
    scraping.scrapingImages(target)
    scraping.scrapingLinks(target)
