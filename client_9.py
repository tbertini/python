import socket

from socket import *

# Establishing connection with server
serverName = '162.243.73.199'
serverPort = 9998
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Server responds
serverResponse = clientSocket.recv(1024).decode()
print(serverResponse, end="")


# Converts a decimal ip into binary (!!!MAY NEED TO HAVE OUR OWN IMPLEMENTATION, LIKE IN PREVIOUS EXERCISE)
def tobinary(ip):
    bytes = ip.split(".")
    binIp = '{0:08b}'.format(int(bytes[0])) + '{0:08b}'.format(int(bytes[1])) + '{0:08b}'.format(int(bytes[2])) \
            + '{0:08b}'.format(int(bytes[3]))
    return binIp


# List containing interfaces and destination address
interfaces = serverResponse.split(",")
binaryDestinationAddress = tobinary(interfaces[len(interfaces) - 1])

result = len(interfaces) - 2  # Setting result to the otherwise value, which is equal to length-2
bestPrefixMatchingCount = 0

# Searching for the longest matching prefix in the given interfaces
for x in range(0, len(interfaces) - 2):
    binIp = tobinary(interfaces[x].split("/")[0])
    count = 0
    for y in range(0, 32):
        if binIp[y] == binaryDestinationAddress[y]:
            count = count + 1
        else:
            break

    # For some reason sometimes when only the first few bits match (less than 8)
    # that is not the correct answer. I don't remember this being a prerequisite for
    # the longest matching prefix though...
    if count > bestPrefixMatchingCount and count >= 8:
        result = x
        bestPrefixMatchingCount = count


# Send result to server
print(result)
clientSocket.send((str(result).encode()))

# Server responds with flag
serverResponse = clientSocket.recv(1024).decode()
flag = serverResponse
print(flag)

clientSocket.close()
