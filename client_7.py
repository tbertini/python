import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9996
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Client sends (random) SEQ and ACK
seq = 5
ack = 9
clientMessage = 'FIN,ACK Seq=' + str(seq) + ' Ack=' + str(ack)
clientSocket.send(clientMessage.encode())
print(clientMessage)

# Server responds (2 messages received)
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end="")

# Client responds with updated seq and ack
seq = serverResponse[-2:].strip()
ack = 10    # I think this ACK is random too, not sure
clientMessage = 'ACK Seq=' + str(seq) + ' ACK=' + str(ack)
clientSocket.send(clientMessage.encode())
print(clientMessage)

# Server responds with flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()
