import socket


s = socket.socket()
s.connect(('192.168.1.241', 2000))


while True:
    print(s.recv(50))
