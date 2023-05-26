from urllib.request import urlopen
import urllib.error


try:
    response = urlopen(input("Enter url: "))
    print(response.read())

except urllib.error.HTTPError as e:
    print("Exception: ", e)
    print("Status", e.status)
    print("Reason", e.reason)
    print("URL", e.url)
