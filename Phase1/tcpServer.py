import socket

serverPort = 12000      # chosen port
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('',serverPort))  # binds socket to host and port
serverSocket.listen(1)              # listens for incoming connection

print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()  # accepts connection
    sentence = connectionSocket.recv(1024).decode() # receives data and decodes it
    
    capitalizedSentence = sentence.upper()              # capitalizes data
    print(f"Data received: {sentence} -> Data returning: {capitalizedSentence}")
    connectionSocket.send(capitalizedSentence.encode()) # encodes and sends back
    
    connectionSocket.close()        # closes socket