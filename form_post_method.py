import requests

data_dictionary = {
    "custname": "customet",
    "custtel": "1234567893",
    "size": "Large",
    "email": "email@gmail.com",
}

response = requests.post("http://httpbin.org/post", data=data_dictionary)

if response.status_code == 200:
    print(response.text)
