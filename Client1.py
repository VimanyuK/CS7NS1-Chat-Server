# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:47:41 2017

@author: Vimanyu
"""

import socket
HOST = socket.gethostname()
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((HOST, 80))
clientsocket.send('hello'.encode('utf-8') )

