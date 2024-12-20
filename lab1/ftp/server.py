# server
"""program and screenshot of output"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
s.bind(('',12345))
s.listen(5)
packet_size = 1024;

c, addr = s.accept()
print("got connection from ", addr)
with open("message.txt","r") as ip:
    text = ip.read(packet_size)
    c.send(text.encode())
c.close()
