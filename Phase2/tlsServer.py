import socket
import ssl

serverPort = 12000

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    print("The TLS server is ready to receive")
    while True:
        tcpConnection, addr = serverSocket.accept()
        print(f"Connection from {addr}, attempting TLS")

        tlsConnection = context.wrap_socket(tcpConnection, server_side=True)

        try:
            sentence = tlsConnection.recv(1024).decode()

            capSentence = sentence.upper()
            print(f"Data recieved: {sentence} -> Data returning: {capSentence}")
            tlsConnection.send(capSentence.encode())
        
        except Exception as e:
            print(f"TLS Error: {e}")
        
        finally:
            tlsConnection.close()
        
if __name__ == "__main__":
    main()