# server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port:=12345))
s.listen(5)
print("socket is listening...")

alphabet = "abcdefghiklmnopqrstuvwxyz"# without j
keyword = "monarchy"
filler = 'x'

def create_grid():
    grid = [ [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ]
    print(grid)
    k1 = 0 
    k2 = 0 
    for i in range(5):
        for j in range(5):
            if k1<len(keyword):
                grid[i][j] = keyword[k1]
                k1+=1
            elif alphabet[k2] in keyword:
                while alphabet[k2] in keyword:
                    k2+=1
                grid[i][j] = alphabet[k2]
                k2+=1
            else:
                grid[i][j] = alphabet[k2]
                k2+=1
    return grid
    
grid = create_grid()
print(grid)

def find_grid(a): # takes a letter return pos
    for i,row in enumerate(grid):
        if a in row:
            return i,row.index(a)

def preprocess(ip: str)->str:
    """remove space and add replace j with i"""
    op = ""
    for x in ip:
        if x==" ":
            pass
        elif x=='j':
            op+='i'
        else:
            op += x
    return op


def split_into_twos(ip: str):
    n = len(ip)
    op = ""
    i = 0
    while i<n:
        if i+1<n:
            if ip[i] == ip[i+1]:
                op+=ip[i]
                op+=filler
                i+=1
            else:
                op+=ip[i]
                op+=ip[i+1]
                i+=2
        else:
            op += ip[i]
            op += filler
            i += 1

    if len(ip)%2 != 0:
        ip+=filler
    n = len(ip)
    op1 = []
    for i in range(0,n,2):
        op1.append(ip[i]+ip[i+1])
    return op1


def cipher(twos):
    op = ""
    for pair in twos:
        xy1 = find_grid(pair[0])
        xy2 = find_grid(pair[1])
        op += grid[xy1[0]][xy2[1]] + grid[xy2[0]][xy1[1]]
    return op

def decipher(twos):
    op = ""
    for pair in twos:
        xy1 = find_grid(pair[0])
        xy2 = find_grid(pair[1])
        op += grid[xy1[0]][xy2[1]] + grid[xy2[0]][xy1[1]]
    return op

while True:
    c, addr = s.accept()
    print("got connection from ", addr)
    while True:
        outgoing = input("enter message >")
        pre_text = preprocess(outgoing)
        twos = split_into_twos(pre_text)
        ciphered = cipher(twos)
        c.send(ciphered.encode())

        incoming = c.recv(1024).decode()
        twos_in = split_into_twos(incoming)
        op = decipher(twos_in)
        print(op)
    c.close()
    break

