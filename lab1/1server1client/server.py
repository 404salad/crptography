# server
"""program and screenshot of output"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created");

port = 12345 

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print("got connection from ", addr)
    c.send("thank you for connecting".encode())
    c.close()
    break
