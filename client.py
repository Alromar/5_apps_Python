import socket
#server in beowser https://realpython.com/python-http-server/
host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((host,port))

# message = sock.recv(1024) #receive bytes

# while message:
#     print("Message: ", message.decode())
#     message = sock.recv(1024)

#2 client server 
fileName = 'abc.txt '
sock.send(fileName.encode())

readFile = sock.recv(1024) #bytes
print(readFile.decode())

sock.close()


