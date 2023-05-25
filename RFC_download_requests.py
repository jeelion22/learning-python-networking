import sys, requests

try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print("must provide valid rfc number as first argument")
    sys.exit(2)

url = "http://www.rfc-editor.org/rfc/rfc{}.txt".format(rfc_number)

rfc_response = requests.get(url).text

print(rfc_response)
