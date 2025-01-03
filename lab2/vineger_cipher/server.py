# server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port:=12345))
s.listen(5)
print("socket is listening...")

alpha = "abcdefghijklmnopqrstuvwxyz"
keyword = "deceptive"

def vcipher(ip: str) -> str:
    op = ""
    i = 0
    k = len(keyword)
    for e in ip:
        op += alpha[(alpha.find(e) + alpha.find(keyword[i%k])) % 26]
        i+=1
    return op

def vdecipher(ip: str) -> str:
    op = ""
    i = 0
    k = len(keyword)
    for e in ip:
        op += alpha[(alpha.find(e) - alpha.find(keyword[i%k])) % 26]
        i+=1
    return op

while True:
    c, addr = s.accept()
    print("got connection from ", addr)
    while True:
        outgoing = input("enter message >")
        ciphered = vcipher(outgoing)
        c.send(ciphered.encode())

        incoming = c.recv(1024).decode()
        print(vdecipher(incoming))
    c.close()
    break

