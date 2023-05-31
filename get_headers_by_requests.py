import requests

url = "https://www.packtpub.com"

response = requests.get(url)  # it is a dictionary object

# prints response headers
print("Response Header:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# prints requests headers
print("\nRequest Header: ")
for key, value in response.request.headers.items():
    print(f"{key}: {value}")
