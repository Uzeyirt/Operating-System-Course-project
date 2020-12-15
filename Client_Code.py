#Uzeyir Topaloglu 2079424
#Esmafer Direybatogullari 2015998
import threading
import os
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5555
BUFFER_SIZE = 1024
##################   CONNECTION 1   ################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

SearchWord = raw_input('Word that you want search:')
DctPath = raw_input(r"File path:") #without 'r' string can be wrong. For example ( c:\\user\\...)

MESSAGE = SearchWord + ' ' + DctPath

s.send(MESSAGE)  #send array through TCP connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #now, client need to receive search results, so it is listenerfor TCP connection
s.bind((TCP_IP, 6666))
s.listen(1)
conn, addr = s.accept()


while 1:
   data = conn.recv(BUFFER_SIZE)
   if not data: break
   print "received data from Server : ", data

##################   CONNECTION 2   ################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

SearchWord = raw_input('Word that you want search:')
DctPath = raw_input(r"File path:") #without 'r' string can be wrong. For example ( c:\\user\\...)

MESSAGE = SearchWord + ' ' + DctPath

s.send(MESSAGE)  #send array through TCP connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #now, client need to receive search results, so it is listenerfor TCP connection
s.bind((TCP_IP, 6666))
s.listen(1)
conn, addr = s.accept()


while 1:
   data = conn.recv(BUFFER_SIZE)
   if not data: break
   print "received data from Server : ", data
##################   CONNECTION 3   ################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

SearchWord = raw_input('Word that you want search:')
DctPath = raw_input(r"File path:") #without 'r' string can be wrong. For example ( c:\\user\\...)

MESSAGE = SearchWord + ' ' + DctPath

s.send(MESSAGE)  #send array through TCP connection

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #now, client need to receive search results, so it is listenerfor TCP connection
s.bind((TCP_IP, 6666))
s.listen(1)
conn, addr = s.accept()


while 1:
   data = conn.recv(BUFFER_SIZE)
   if not data: break
   print "received data from Server : ", data