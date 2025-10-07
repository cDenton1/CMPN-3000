# data checker UDP client, project 1 data communications
import socket

serverName = '10.0.2.15' # other kali vm IP address
serverPort = 4444   # chosen port

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    num = input('ENTER NUMBER: ')

    clientSocket.sendto(num.encode(), (serverName, serverPort))
    result, serverAddress = clientSocket.recvfrom(2048)

    print(result.decode())

finally:
 clientSocket.close()