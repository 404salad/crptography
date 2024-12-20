# server
"""program and screenshot of output"""
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created");
port = 12345

s.bind(('',port))
print("socket binded to %s" %(port))
s.listen(5)
print("socket is listening")

def client_listener(c, addr):
    print("got connection from ", addr)
    while True:
        text = input("enter message ->:")
        c.send(text.encode())
        print(c.recv(1024).decode())
    c.close()

while True:
    c, addr = s.accept()
    threading.Thread(target=client_listener, args=(c,addr)).start()
