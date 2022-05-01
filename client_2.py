import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9991
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Client sends message to server
message = 'helo'
print(message)
clientSocket.sendto(message.encode(), (serverName,serverPort))

# Flag
serverResponse, serverAddress = clientSocket.recvfrom(1024)
flag = serverResponse
print(flag)

clientSocket.close()
