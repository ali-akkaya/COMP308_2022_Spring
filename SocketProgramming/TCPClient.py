from socket import *

serverName = 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)  # The first parameter again indicates that the underlying network is
# using IPv4. The second parameter indicates that the socket is of type SOCK_STREAM, which means it is a TCP socket.
clientSocket.connect((serverName, serverPort))  # This line initiates the TCP connection between the client and
# server. The parameter of the 'connect()' method is the address of the server side of the connection. After this line
# of code is executed, the three-way handshake is performed and a TCP connection is established between the client
# and server.
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())  # Note that the program does not explicitly create a packet and attach
# the destination address to the packet, as was the case with UDP sockets. Instead the cli- ent program simply drops
# the bytes in the string sentence into the TCP connection.
modifiedSentence = clientSocket.recv(1024)  # The client then waits to receive bytes from the server.
print('From Server: ', modifiedSentence.decode())
clientSocket.close()
