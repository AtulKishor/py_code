import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'data.pr4e.org'
port = 80
mysock.connect((host, port))
f = 'http://data.pr4e.org/intro-short.txt'
cmd = ('GET '+f+' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)#returns no of bytes sent

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
