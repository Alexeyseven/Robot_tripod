import socket


s = socket.socket()
s.connect(('192.168.1.241', 2000))


while True:
    mes = s.recv(50)
    s.send(mes)
