import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9990
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()