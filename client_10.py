import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Server responds
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end="")

# Calculating the checksum
byte0 = serverResponse.split()[0]
byte1 = serverResponse.split()[1]

# (NEEDS TO BE FIXED: NEED OUR OWN BINARY ADDITION METHOD)
# Converting bytes to int to sum them and then converting to binary using python builtins
sum = int(byte0, 2) + int(byte1, 2)
sum = '{0:08b}'.format(sum)

# When an overflow at the last bit happens, we need to add that remainder to the first bit
while len(str(sum)) == 9:
    sum = int(str(sum[1:9]), 2) + int("1", 2)
    sum = '{0:08b}'.format(sum)

# Flip all the bits, for 1's complement
result = ""
for x in range(0, len(sum)):
    if sum[x] == "0":
        result = result + "1"
    else:
        result = result + "0"


# Send response to server
print(result)
clientSocket.send(result.encode())


# Server responds with flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()
