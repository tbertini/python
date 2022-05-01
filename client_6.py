import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9995
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Client sets SYN to 0 and sends it
synSeq = 'SYN Seq=0'
print(synSeq)
clientSocket.send(synSeq.encode())

# Server responds with SYN, ACK numbers
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end="")
# Server's ACK number, saving it this way in case it's not always 1
# Removing the \n at the end using .strip()
serverACK = serverResponse[serverResponse.rfind('=')+1:].strip()

# Client responds with ACK
ack = 'ACK Seq=' + serverACK + ' ACK=' + serverACK
print(ack)
clientSocket.send(ack.encode())

# Server responds with flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()