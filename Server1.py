# task to implimplement
# 1.Join
# 2.chat
# 3.message
# 4.leave
# 5.Disconnect


import socket
from threading import Thread
import random
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5555
print ('Socket created')
 
#Bind socket to local host and port
try:
    server.bind((host, port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()     
print ('Socket bind complete')

print("Host name: ",host)

#Start listening on socket
while True:
    server.listen(5)
    conn, ip = server.accept()
    #monitoring connections
    conn.send("Connected to the server".encode('utf-8') )
    print("Connected to ",ip)
    data = conn.recv(2048)
   # printing the message received from the client
    print(data)
   


