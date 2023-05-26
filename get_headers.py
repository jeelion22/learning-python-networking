from urllib.request import urlopen

url = input("Enter the URL that you want to read: ")

http_response = urlopen(url)

# print(http_response)

if http_response.status == 200:
    print("\nreponse headers using the attribute 'headers' of the response object\n")
    print(http_response.headers)

    print("The response header using getheaders() method\n")
    # it return as a list of tuples containing header_name:header_value pair
    for key, value in http_response.getheaders():
        print(key, value)
