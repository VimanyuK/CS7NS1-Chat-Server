# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:47:41 2017

@author: Vimanyu
"""

import socket
host = socket.gethostname()
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect((host, 5555))
data = clientsocket.recv(2048)
print (data)
# to send message to the server
msg = input("-->")
clientsocket.send(msg.encode('utf-8') )

clientsocket.close()

