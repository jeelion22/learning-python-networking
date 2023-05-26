import requests
from bs4 import BeautifulSoup

response = requests.get("http://127.0.0.1:8080/")

if response.status_code == 200:
    print(response.headers)
    print(response.text)
print(response.headers["server"])
