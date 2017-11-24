import socket 
import sys,os
from threading import Thread

# client side functions to respond to the server
def join():
    chatroom = input('chatroom: ')
    conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
    conn_msg += "CLIENT IP: \n".encode('utf-8')
    conn_msg += "PORT: \n".encode('utf-8')
    conn_msg += "CLIENT_NAME:".encode('utf-8') + client_name.encode('utf-8') + "\n".encode('utf-8')
    clientsocket.send(conn_msg)
    
def chat(s):
    chat_room = input('Which room to send message? ')
    chat_message = input('Enter Message to send: ')
    msg = "CHAT: ".encode('utf-8') + chat_room.encode('utf-8') + "\n".encode('utf-8')
    msg += "JOIN_ID: ".encode('utf-8') + str(jID).encode('utf-8') + "\n".encode('utf-8')
    msg += "CLIENT_NAME: ".encode('utf-8') + client_name.encode('utf-8') + "\n".encode('utf-8')
    msg += "MESSAGE: ".encode('utf-8') + chat_message.encode('utf-8') + "\n\n".encode('utf-8')
    s.send(msg)
    
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
    
    
    