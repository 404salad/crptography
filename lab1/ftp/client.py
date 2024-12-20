import socket
s = socket.socket()
s.connect(("127.0.0.1", 12345))
packet_size = 1024
untill = True

file = []
while untill: 
    rec = s.recv(packet_size).decode()
    file.append(rec)
    if rec == "":
        break
with open("output.txt", "w") as op:
    op.writelines(file)
    op.close()
s.close()

