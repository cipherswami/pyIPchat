import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = input("Enter server IP: ")
ADDR = (SERVER, PORT)
key = 1010

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    client.send(msg.encode(FORMAT))
    print(type(msg.encode(FORMAT)))

send(input("Enter the Message: "))
