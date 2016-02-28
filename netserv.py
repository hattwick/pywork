# Python3 Server Test
# 2016
__learner__ = 'Hattwick'

import socket
size = 1500
host = ''
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP Connection
sock.setsockopt(socket.SOL_SOCKET, sock.SO_REUSEADDR, 1)   # create socket

sock.bind((host,port))
sock.listen(5)


