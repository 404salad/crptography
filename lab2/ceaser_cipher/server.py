# server
"""program and screenshot of output"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port:=12345))
s.listen(5)
print("socket is listening...")

alphabet = ['a','b','c','d','e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = 5

def ceaser(ip:str)->str:
    op = ""
    for x in ip:
        if x==" ":
            op += " "
        else:
            op += alphabet[(ord(x)-ord('a')+key)%26]
    return op

def de_ceaser(ip:str)->str:
    op = ""
    for x in ip:
        if x==" ":
            op+=" "
        else:
            op += alphabet[(ord(x)-ord('a')-key+26)%26]
    return op

while True:
    c, addr = s.accept()
    print("got connection from ", addr)
    while True:
        text = input("enter message :")
        c.send(ceaser(text).encode())
        response = c.recv(1024).decode()
        print(response + "->" + de_ceaser(response))
    c.close()
    break

