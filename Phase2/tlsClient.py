import socket
import ssl

serverName = '10.0.2.15'
serverPort = 12000

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    context.load_verify_locations("server.crt")
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tlsSocket = context.wrap_socket(clientSocket, server_hostname=serverName)

    try:
        tlsSocket.connect((serverName, serverPort))
        
        sentence = input("Input lowercase sentence: ")
        tlsSocket.send(sentence.encode())

        modifiedSentence = tlsSocket.recv(1024).decode()
        print("From Server:", modifiedSentence)

    except ssl.SSLError as e:
        print(f"TLS certification verification failed: {e}")

    finally:
        tlsSocket.close()

if __name__ == "__main__":
    main()
