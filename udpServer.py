import socket

serverPort = 12000      # chosen port
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSocket.bind(('', serverPort))     # binds socket to host and port

print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)    # receives data
    modifiedMessage = message.decode().upper()              # decodes and capitalizes data
    
    print(f"Data received: {message} -> Data returning: {modifiedMessage}")
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)    # encodes and sends back