import socket
s = socket.socket()
port = 12345
s.connect(("127.0.0.1", port))
while True: 
    print(s.recv(1024).decode())
    text = input("enter message:>:")
    s.send(text.encode())
s.close()
