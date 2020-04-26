#!/usr/bin/python
import socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("",3000))

while 3<4:
	recieve = ""
	recieve = (x.recvfrom(1000))[0]
	#ip = recieve[1][0]
	#port =int(recieve[1][1])
	print "sender::   "+recieve
	if(len(recieve)>0):
		reply = raw_input("you::  ")
		x.sendto(reply,("192.168.145.132",2000))
	
	
		
		
