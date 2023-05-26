import socket

sock = socket.socket()
print("socket created")

port = 80
sock.bind(("", port))
print(f"socket binded to the port {port}")

sock.listen(5)
print("socket is listening...")

while True:
    conn, addr = sock.accept()
    print(f"Got message from {addr}")

    conn.send(b"You are connected")
    sock.close()
