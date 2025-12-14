import socket
import ssl

serverName = '10.0.2.15'    # server IP address
serverPort = 12000          # chosen port 

def main():                 # main function, makes future modularity easier
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)                           # SSL context for TLS client

    context.load_verify_locations("ca.crt")                                     # trusted certificate is loaded
    context.verify_mode = ssl.CERT_REQUIRED                                     # requires server certificate verification
    context.check_hostname = True                                               # requires hostname verification

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            # creates TCP socket
    tlsSocket = context.wrap_socket(clientSocket, server_hostname=serverName)   # wraps TCP socket in TLS

    try:
        tlsSocket.connect((serverName, serverPort))             # connects to server
        
        sentence = input("Input lowercase sentence: ")          # stores user input
        if not sentence:                                        # prevent empty input
            print("Error: input cannot be empty")
            return
        if len(sentence) > 1024:                                # prevent oversized payload
            print("Error: input too long")
            return

        tlsSocket.send(sentence.encode())                       # encodes and sends data

        modifiedSentence = tlsSocket.recv(1024).decode()        # receives data, max 1024 bytes, and decodes it
        print("From Server:", modifiedSentence)                 # prints received data

    except ssl.SSLError as e:                                   # catches TLS/SSL errors
        print(f"TLS certification verification failed: {e}")    # displays error

    finally:
        tlsSocket.close()   # closes socket

if __name__ == "__main__":
    main()
