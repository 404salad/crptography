import socket
s = socket.socket()
s.connect(("127.0.0.1", 12345))

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
    print(de_ceaser(s.recv(1024).decode()))
    text = input("enter message :")
    s.send(ceaser(text).encode())

s.close()
