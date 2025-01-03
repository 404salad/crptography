# server
"""program and screenshot of output"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
print("socket successfully created");
port = 12345 

s.bind(('',port))
print("socket binded to %s" %(port))

s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept()
    print("got connection from ", addr)
    while True:
        text = input("enter message ->:")
        c.send(text.encode())
        print(c.recv(1024).decode())
    c.close()
    break
