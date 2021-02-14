import socket
import threading
import time

HEADER = 64
PORT = 10001
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.35.59"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("Connected by", ADDR)

#def send(msg):
#    message = msg.encode(FORMAT)
#    msg_length = len(message)
#    send_length = str(msg_length).encode(FORMAT)
#    send_length += b' ' * (HEADER - len(send_length))
#    client.send(send_length)
#    client.send(message)
copy = '0'
while True:
        f = open('./coordinates/coordinates.txt', 'r')
        s = f.read()
        f.close()

        if copy == s :
            continue
        else :
            print('coordinates : ', s)
            copy = s
            client.sendall(s.encode())

client.close()