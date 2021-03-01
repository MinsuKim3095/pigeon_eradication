import socket
import RPi.GPIO as GPIO
import time
from time import sleep

HOST = '192.168.35.59'
PORT = 10001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

client, addr = server.accept()
print("Connected by", addr)

copy = '0'
while True:
	data = client.recv(1024)
	#if data == None:
		
	#if copy == data:
		#continue
	#else :
	print('coordinates : ', repr(data.decode()))
	copy = data
	f = open('/home/minsu/coordinates.txt', 'w')
	f.write(data.decode())
	f.close()


server.close()
