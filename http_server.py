import http.server
import socketserver

port = 8080

handler = http.server.SimpleHTTPRequestHandler

http = socketserver.TCPServer(("localhost", port), handler)

print("serving at port", port)


http.serve_forever()
