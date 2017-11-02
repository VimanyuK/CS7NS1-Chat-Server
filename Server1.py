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
port = 80
print ('Socket created')
 
#Bind socket to local host and port
try:
    server.bind((host, port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()     
print ('Socket bind complete')

print(host)

#Start listening on socket
while True:
    server.listen(5)
    conn, ip = server.accept()
    #monitoring connections
    print("Connected to ",port,ip)





