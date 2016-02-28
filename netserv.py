# Python3 Server Test
# 2016
__learner__ = 'Hattwick'

import socket
size = 1500
host = ''
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP Connection
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # create socket

sock.bind((host,port))
sock.listen(5)

client, addr = sock.accept()
data = c.recv(size)
if data:
	f = open("inboundstorage.dat", '+w')     # save received data to file
	print(addr[0], ' has connected')
	f.write(addr[0])
	f.write(":")
	f.write(data.decode("utf-8"))
	f.close()
sock.close()