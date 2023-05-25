import sys, urllib.request

try:
    # sys.argv[1] is used when the file is opened through
    # terminal by providing the input as first argument
    # python3 <file_name.py> <arg>
    rfc_number = int(sys.argv[1])

except (IndexError, ValueError):
    print("Must supply RFC number as first argument")

url = "http://www.rfc-editor.org/rfc/rfc{}.txt".format(rfc_number)

rfc_raw = urllib.request.urlopen(url).read()

rfc_text = rfc_raw.decode()

print(rfc_text)
