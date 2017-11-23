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

threadLock = Lock()

def join(conn_msg,csock):
    
    threadLock.acquire()
    gname = conn_msg.find('JOIN_CHATROOM:'.encode('utf-8'))+15
    gname_end = conn_msg.find('\n'.encode('utf-8'))
    groupname = conn_msg[gname:gname_end]
    
    cname = conn_msg.find('CLIENT_NAME'.encode('utf-8'))+13
    cname_end = conn_msg.find(' '.encode('utf-8'),cname)
    clientname = conn_msg[cname:cname_end]
    rID = 0
    if (groupname.decode('utf-8')) == 'room1' :
        g1_clients.append(clThread.socket)
        rID = 1001
    elif groupname == 'room2' :
       g2_clients.append(clThread.socket)
       rID = 1002
	#sending ackowledgement
    response = "JOINED_CHATROOM: ".encode('utf-8') + groupname+ "\n".encode('utf-8')
    response += "SERVER_IP: ".encode('utf-8') + host.encode('utf-8') + "\n".encode('utf-8')
    response += "PORT:".encode('utf-8') + str(port).encode('utf-8') + "\n".encode('utf-8')
    response += "ROOM_REF: ".encode('utf-8') + str(rID).encode('utf-8') +'\n'.encode('utf-8')
    response += "JOIN_ID: ".encode('utf-8') + str(clThread.uid).encode('utf-8') + "\n".encode('utf-8')
    csock.send(response)
    grpmessage = "CHAT:".encode('utf-8') + str(rID).encode('utf-8') + "\n".encode('utf-8')
    grpmessage += "CLIENT_NAME:".encode('utf-8') + clientname + "\n".encode('utf-8') 
    grpmessage += "MESSAGE:".encode('utf-8') + clientname + "\n".encode('utf-8') 
    grpmessage += "CLIENT_ID:".encode('utf-8') + str(clThread.uid).encode('utf-8') +"\n".encode('utf-8')
    grpmessage += "JOINED_GROUP".encode('utf-8') +"\n".encode('utf-8')
    if (groupname.decode('utf-8')) == 'room1':
        for x in range(len(g1_clients)):
            g1_clients[x].send(grpmessage)
    elif (groupname.decode('utf-8')) == 'room2':
        for x in range(len(g2_clients)):
            g2_clients[x].send(grpmessage)
        threadLock.release()
    return groupname,clientname,rID


def chat(conn_msg,csock):
    pass
def resp(msg,socket):
    pass
def leave(conn_msg,csock):
    pass
def check_msg(msg):
    pass

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
	def run(self):
		while True:
			print("Starting again")
			conn_msg = conn.recv(1024)
			print('CM')
			print(conn_msg)
			cflag = check_msg(conn_msg)
			if cflag == 1 : self.roomname,self.clientname,self.roomID = join(conn_msg,conn)
			elif cflag == 2 : leave(conn_msg,conn)
			elif cflag == 3 : return(0)
			elif cflag == 4 : chat(conn_msg,conn)
			elif cflag == 5 : resp(conn_msg,conn)
			else : print('Error code. Wait for more')
			self.chatroom.append(self.roomname)
			print('Total clients in group g1: ')
			print(len(g1_clients))
			print('Total clients in group g2: ')
			print(len(g2_clients))


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
    
    
    