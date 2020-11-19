# -*- coding: utf-8 -*-

print("exercise 3 - Exploring the HyperText Transport Protocol")
#basic code is in the part 2 document I saved
#where to get data: http://data.pr4e.org/intro-short.txt
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
 
while True:
    data = mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode(),end='')
mysock.close()
 
#this is the socket1.py program
#import socket
 
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#while True:
    #data = mysock.recv(512)
    #if len(data) < 1:
    #    break
    #print(data.decode(),end='')
 
#mysock.close()