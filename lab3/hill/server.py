# server
"""program and screenshot of output"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port:=12345))
s.listen(5)
print("socket is listening...")

key = [
    [17,17,5],
    [21,18,21],
    [2,2,19]
]

alpha = "abcdefghijklmnopqrstuvwxyz"

inverse_key = []
for row in key:
    #note to make deepcopy use row[:]
    inverse_key.append(row[:])

def find_inverse(n):
    for i in range(26):
        if (n*i)%26==1:
            return i

#################################################################################################################33
# finding adjoint (works!!!)
adj = []
for row in key:
    #note to make deepcopy use row[:]
    adj.append(row[:])

for row in range(3):
    for col in range(3):
        next_row = (row+1)%3
        next_next_row = (next_row+1)%3
        rows = [next_row, next_next_row]
        adj[row][col] = (key[rows[0]][(col+1)%3]* key[rows[1]][(col+2)%3] - key[rows[0]][(col+2)%3]* key[rows[1]][(col+1)%3]);
                

# finding determinant
det = 0
row =0
for col in range(3):
    next_row = (row+1)%3
    next_next_row = (next_row+1)%3
    rows = [next_row, next_next_row]
    det += (key[row][col]*(key[rows[0]][(col+1)%3]* key[rows[1]][(col+2)%3] - key[rows[0]][(col+2)%3]* key[rows[1]][(col+1)%3]));

det = det%26

# transpose adj
tran_adj = []
for row in adj:
    #note to make deepcopy use row[:]
    tran_adj.append(row[:])

for row in range(3):
    for col in range(3):
        tran_adj[row][col] = adj[col][row]

#finding inverse

detinv = find_inverse(det)
for row in range(3):
    for col in range(3):
        inverse_key[row][col] = (tran_adj[row][col] * detinv)%26;

#################################################################################################################

    
print(key)
print(adj)
print(tran_adj)
print(det)
print(detinv)
print(inverse_key)

def hill(ip:str)->str:
    op = ""
    # adjusting for 3 ki divisilibity
    ip+='x'*((3-(len(ip)%3))%3)
    words = []
    for i in range(0,len(ip),3):
        words.append(ip[i:i+3])
    for word in words:
        for col in range(3):
            wordsum = 0
            for row in range(3):
                wordsum += alpha.find(word[row])*key[row][col]
            op += alpha[wordsum%26]
    return op


def de_hill(ip:str)->str:
    op = ""
    words = []
    for i in range(0,len(ip),3):
        words.append(ip[i:i+3])
    for word in words:
        for col in range(3):
            wordsum = 0
            for row in range(3):
                wordsum += alpha.find(word[row])*inverse_key[row][col]
            op += alpha[wordsum%26]
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
    c, addr = s.accept()
    print("got connection from ", addr)
    while True:
        text = input("enter message ->")
        text = preprocess(text)
        c.send(hill(text).encode())
        response = c.recv(1024).decode()
        print(response + "->" + de_hill(response))
    c.close()
    break

