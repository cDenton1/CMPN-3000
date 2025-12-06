import socket

serverName = '10.0.2.15'    # server IP address
serverPort = 12000          # chosen port

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((serverName,serverPort))   # connects to server
sentence = input('Input lowercase sentence:')   # stores user input
clientSocket.send(sentence.encode())            # encodes and sends data

modifiedSentence = clientSocket.recv(1024)          # receives data, max 1024 bytes
print ('From Server:', modifiedSentence.decode())   # decodes and prints data

clientSocket.close()        # closes socket
