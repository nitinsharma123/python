#!/usr/bin/python
import socket

y=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
y.bind(("",2000))
recieve = "a"
while 3<4 :
	if(len(recieve)>0):
		a= raw_input("you::      ")
		x=y.sendto(a,("192.168.145.133",3000))
		recieve = "" 
		recieve=y.recvfrom(1000)
		recieve=recieve[0]
		print("sender::   "+recieve)
