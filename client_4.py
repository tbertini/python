import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9993
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Server responds
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end="")

# Saving all of the server's returned data into a list, splitting all values by the spaces in between
dataList = serverResponse.split()

# Saving all values, removing unnecessary parts like 'ms'
estRTT = int(dataList[0][:-2])
alpha = float(dataList[1])
sampleRTT = int(dataList[2][:-2])

# Calculating the estimated RTT
newEstRTT = str(round((1-alpha)*estRTT + alpha*sampleRTT))
print(newEstRTT)
clientSocket.sendto(newEstRTT.encode(), (serverName,serverPort))

# Flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()