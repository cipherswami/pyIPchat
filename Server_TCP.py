import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
key = 1010

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f"[#] Server is Runnig on {SERVER}")

[conn, addr] = server.accept()

msg = conn.recv(1024).decode(FORMAT)
print(f"Received: {msg}")