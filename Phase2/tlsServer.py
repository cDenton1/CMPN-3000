import socket
import ssl

serverPort = 12000      # chosen port

def main():             # main function, makes future modularity easier
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)                       # SSL context for TLS server
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")    # server certificate and private key are loaded

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # creates TCP socket
    serverSocket.bind(('', serverPort))                                     # binds socket to host and port
    serverSocket.listen(1)                                                  # listens for incoming connection

    print("The TLS server is ready to receive")
    while True:
        tcpConnection, addr = serverSocket.accept()                                 # accepts connection
        print(f"Connection from {addr}, attempting TLS")
        tlsConnection = context.wrap_socket(tcpConnection, server_side=True)        # wraps connection in TLS

        try:
            sentence = tlsConnection.recv(1024).decode()                            # receives data, max 1024 bytes, and decodes it
            if not sentence:                                                        # close if received empty data
                print("Empty message received, closing connection")
                return

            capSentence = sentence.upper()                                          # capitalizes data
            print(f"Data recieved: {sentence} -> Data returning: {capSentence}")
            tlsConnection.send(capSentence.encode())                                # encodes and sends back
        
        except Exception as e:          # catches exceptions
            print(f"TLS Error: {e}")    # displays
        
        finally:
            tlsConnection.close()       # close socket
        
if __name__ == "__main__":
    main()