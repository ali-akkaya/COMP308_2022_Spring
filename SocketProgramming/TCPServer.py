from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))  # we associate the server port number, serverPort, with this socket. But with
# TCP, serverSocket will be our welcoming socket.
serverSocket.listen(1)  # After establishing this welcoming door, we will wait and listen for some client to knock on
# the door. This line has the server listen for TCP connection requests from the client. The parameter specifies the
# maximum number of queued connections (at least 1).
print('The server is ready to receive')
while True:
    connectionSocket, address = serverSocket.accept()  # When a client knocks on this door, the program invokes the
    # 'accept()' method for serverSocket, which creates a new socket in the server, called 'connectionSocket',
    # dedicated to this particular client.
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    #connectionSocket.close()  # After sending the modified sentence to the client, we close the connection socket.
    # But since 'serverSocket' remains open, another client can now knock on the door and send the server a sentence to
    # modify.
