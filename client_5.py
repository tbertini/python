import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9994
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Server responds
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end = "")
dataListRaw = serverResponse.split()


# Where should functions be defined in python? lol
def to_bits(number, unit):
    multiplier = {'bits': 1, 'Kb': 1000, 'Mb': 1000000, 'Gb': 1000000000, 'Kbps': 1000,
                  'Mbps': 1000000, 'Gbps': 1000000000}
    return(number*multiplier[unit])


L= to_bits(int(dataListRaw[0][2:]), dataListRaw[1])
R1 = to_bits(int(dataListRaw[2][3:]), dataListRaw[3])
R2 = to_bits(int(dataListRaw[4][3:]), dataListRaw[5])

# Calculating the total delay in seconds
totalDelay = (L/R1 + L/R2)
print(totalDelay)

# Send the answer to the server
clientSocket.send(str(totalDelay).encode())

# Flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()









