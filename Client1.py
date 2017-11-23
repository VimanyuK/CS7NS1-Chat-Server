import socket 
import sys,os
from threading import Thread

# client side functions to respond to the server
def join():
    pass
def chat():
    pass
def leave():
    pass
def disconnect():
    pass
#client thread
class Client_Thread(Thread):
    def __init__(self,socket):
        Thread.__init__(self)
        self.socket = socket
        print('Listening to server')
    def run(self):
        while True:
            data = self.socket.recv(1024)
            print('Message from Client: ')
            print(data.decode(encoding='utf-8'))

#creating the socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#taking the host name from the user
host = input('Host Name: ')
#taking the port number from the user
port = input('Port Number: ')
#connecting to the host 
clientsocket.connect((host, int(port)))

#taking the client name from the user
client_name = input('enter the client name: ')
join()
join_id=0
#receiving the server response
recvd_msg = clientsocket.recv(1024)
#checking for the "JOINED" statement in the received message from the server
chck_msg = recvd_msg.find(b'JOINED')
#assigning the join id to the client
if chck_msg == 0:
   jID_start = recvd_msg.find('JOIN_ID'.encode('utf-8'))+9
   jID_end = recvd_msg.find('\n'.encode('utf-8'),jID_start)-1
   jID = str(recvd_msg[jID_start:jID_end])

server_thread = Client_Thread(clientsocket)
server_thread.start()

while(1):
    print('Enter Option to choose:')
    print('1. Join')
    print('2. Chat')
    print('3. Leave')
    print('4. Disconnect')
    task = input('')
    if task == '1':
        join()
    elif task == '2':
        chat(clientsocket)
    elif task == '3':
        leave(clientsocket)
    elif task == '4':
        disconnect()
    elif task == '5':
        print('Error')
    
    
    