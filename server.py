import socket
import sys

# create a TCP/IP socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind socket to port
mysock.bind(('192.168.56.1',998))

#listen for incoming connection (upto 1 connection with this socket)
mysock.listen(1)
print('waiting for request...')

#wait for connection (till a client socket or 'conn' arrives)
conn, client_address = mysock.accept()
print('connection from: ',client_address)
'''
#file = open('f.txt')
conn.send('Dekh lo bhej diye hai : \r\n\r\n'.encode())		#file.read().encode()+b'\r\n')
'''
flag = True
try:
    while True:
        msg = conn.recv(512).decode()   #first client sends either a message or a get/post/put etc. request
        conn.send((input(msg)+'\r\n').encode()) #print request of client and respond back to client socket **could use sendall method too
        if flag:
            conn.send('enter "quit" to end chat\r\n'.encode())
            flag = False
        if msg == 'quit\r\n':
            break
except:
    pass

mysock.close()

#no need to close client socket here
#for closing client socket , use:
#conn.shutdown(SHUT_WR)