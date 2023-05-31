import urllib.request, urllib.parse, urllib.error

"""use of proxy server for the resource retrival from
the webserver
"""

url = "https://www.github.com"
protocol = "http"
# proxy serber ip addr and its port are separated by colons
proxy_address = "165.24.10.8:8080"

if __name__ == "__main__":
    # pass a parameter as a dictionary containg the key as http protocol
    # and the value as a proxy server
    proxy = urllib.request.ProxyHandler({protocol: proxy_address})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)

    resp = urllib.request.urlopen(url)
    print("\nResponse Headers:\n", resp.headers)

    # get content type
    print(resp.getheader("Content-type"))
