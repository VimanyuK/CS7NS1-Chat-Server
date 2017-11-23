# task to implimplement
# 1.Join
# 2.chat
# 3.message
# 4.leave
# 5.Disconnect


import socket
from threading import Thread
from threading import Lock
import random
import sys

#creating threads for clients   
class client_threads(Thread):

	def __init__(self,ip,port,socket):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.chatroom =[] 
		self.socket = socket
		self.uid = random.randint(1000,2000)
		self.roomname = ''
		self.clientname = ''
		self.roomID = ''


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 5555
#Bind socket to local host and port
try:
    server.bind((host, port))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()     

thread_count = [] 
g1_clients = []
g2_clients = []
print('Server started')
print("Host name: ",host)

#Start listening on socket
while True:
    server.listen(5)
    (conn,(ip,port)) = server.accept()
    print("Connected to ",ip)
    clThread = client_threads(ip,port,conn)
    clThread.start()
    thread_count.append(clThread)
    
    
    