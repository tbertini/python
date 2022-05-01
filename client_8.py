import math
import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9997
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Server responds
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end="")
mask = int(serverResponse.split()[1])
ip = serverResponse.split()[0]
bytes = ip.split(".")

# Calculating network address
# 1) Convert IP to binary (NEEDS TO BE FIXED: WE NEED OUR OWN FUNCTION FOR THIS)
binIp = '{0:08b}'.format(int(bytes[0])) + '{0:08b}'.format(int(bytes[1])) + '{0:08b}'.format(int(bytes[2]))\
        + '{0:08b}'.format(int(bytes[3]))
# 2) Flipping the bits mask to 32 to 0 (as per definition in order to get the network address)
binIp = list(binIp)
for x in range(mask, len(binIp)):
    binIp[x] = "0"

binIp = "".join(binIp)

# 3) Converting from binary to decimal (NEEDS TO BE FIXED: WE NEED OUR OWN FUNCTION FOR THIS)
#    Then adding a dot in between the numbers to get to the network address
binIp = str(int(binIp[0:8], 2)) + "." + str(int(binIp[8:16], 2)) + "." + str(int(binIp[16:24], 2))\
        + "." + str(int(binIp[24:32], 2))


# Sending the network address to the server
print(binIp)
clientSocket.send(binIp.encode())


# Server responds with flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()


