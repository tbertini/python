import socket

from socket import *

# Establish first TCP connection to port 9992
serverName = '162.243.73.199'
serverPort = 9992
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Server responds
serverResponse = clientSocket.recv(1024)
newPort = int(serverResponse.decode()[12:])
print(serverResponse.decode(), end="")

# Close the fist TCP connection
clientSocket.close()

# Open a new TCP connection, this time to the new port
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, newPort))

# Flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()