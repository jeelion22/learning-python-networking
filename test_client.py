import socket

sock = socket.socket()

port = 80

sock.connect(("localhost", port))

print(sock.recv(1024).decode())
sock.close()
