import socket
HOST ='127.0.0.1'
PORT =9999
with sockets.sockets(sockets.AF_INET,sockets.SOCK_STREAM)as s 
s.connect(HOST,PORT)
s.sendall(b'Hello,Server')
data = s.recv(1024)
print ('Receicved', repr(data))