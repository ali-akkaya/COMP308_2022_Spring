from socket import *

serverName = '95.183.227.97'  # Provide string containing either IP address of the server or the host name. If we use host
# name DNS lookup will automatically be performed to get the IP address.
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # The first parameter indicates the address family. 'AF_INET' indicates
# that the underlying network using IPv4. The second parameter indicates that the socket is of type SOCK_DGRAM,
# which means it is a UDP socket.
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))  # We first convert the message from string type to
# byte type, as we need to send bytes into a socket. The method sendto() attaches the destination address (
# serverName, serverPort) to the message and sends the resulting packet into the process’s socket.

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  # The variable serverAddress contains both the server’s
# IP address and the server’s port number. The method 'recvfrom' also takes the buffer size 2048 as input.
print(modifiedMessage.decode())
clientSocket.close()
