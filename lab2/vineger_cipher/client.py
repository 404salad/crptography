#client
import socket
s = socket.socket()
s.connect(("127.0.0.1", 12345))

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

def preprocess(ip: str)->str:
    """remove space """
    op = ""
    for x in ip:
        if x==" ":
            pass
        else:
            op += x
    return op

while True: 
    incoming = s.recv(1024).decode()
    op = vdecipher(incoming)
    print(op)
    outgoing = preprocess(input("enter message >"))
    ciphered = vcipher(outgoing)
    s.send(ciphered.encode())

s.close()
