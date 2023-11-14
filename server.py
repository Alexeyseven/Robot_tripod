import socket


s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(1)
conn, addr = s.accept()

conn.send(b'1')
print(conn.recv(50))