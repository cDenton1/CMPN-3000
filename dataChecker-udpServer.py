# data checker UDP server, project 1 data communications
import socket

serverPort = 4444
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(('', serverPort))
print('SERVER READY')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    revNum = int(message.decode())
    if revNum % 2 == 0:                 # check if the passed input is even
        result = f"{revNum} is EVEN"    # even message for client
    else:                               # else if odd
        result = f"{revNum} is ODD"     # odd message for client

    serverSocket.sendto(result.encode(), clientAddress)