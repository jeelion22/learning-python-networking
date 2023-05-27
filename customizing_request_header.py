from urllib.request import Request, urlopen


url = "http://www.debian.org"

req = Request(url)

# customizing the request header
# resuests the server that the response from it be in the specifided
# language
req.add_header("accept-language", "nl")

res = urlopen(req)

print("\nRequest's Header Items:\n")

# prints the header items of the request
print(req.header_items())
print("\nResponse's headers:\n")
# prints the response header
print(res.headers)
