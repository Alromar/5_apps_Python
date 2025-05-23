#1 server
import socket

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #UDP = .SOCK_DGRAM

sock.bind((host,port))

sock.listen(1)

print("The server is running and is listening to clients requests")
conn, address = sock.accept()

# message = "He there is something important for you"

# conn.send(message.encode())

#2 file server toevoegen bij versturen
print("Connection has been established with ",str(address))
try:
    fileName = conn.recv(1024)
    file = open(fileName, 'rb')
    readFile = file.read()
    conn.send(readFile)
    
    file.close()
except:
    conn.send("File not found on the server". encode())
conn.close()
# einde 1