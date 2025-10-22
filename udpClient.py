import socket

serverName = '10.0.2.15'    # server IP address
serverPort = 12000          # chosen port

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input('Input lowercase sentence: ')                       # stores user input
clientSocket.sendto(message.encode(), (serverName, serverPort))     # encodes and sends data to server and port

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)        # receives data, max 2048 bytes
print('From Server:', modifiedMessage.decode())                     # decodes and prints data

clientSocket.close()        # closes socket
