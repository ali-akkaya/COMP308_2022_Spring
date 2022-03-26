from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  # The first parameter indicates the address family. 'AF_INET' indicates
# that the underlying network using IPv4. The second parameter indicates that the socket is of type SOCK_DGRAM,
# which means it is a UDP socket.
serverSocket.bind(('', serverPort))  # 'binds' (that is, assigns) the port number 12000 to the server’s
# socket. Thus, in UDPServer, the code (written by the application developer) is explicitly assigning a port number
# to the socket. In this manner, when anyone sends a packet to port 12000 at the IP address of the server,
# that packet will be directed to this socket.
print('The server is ready to receive')
while True:  # UDPServer waits for a packet to arrive.
    message, clientAddress = serverSocket.recvfrom(2048)  # When a packet arrives at the server’s socket,
    # the packet’s data is put into the variable message and the packet’s source address is put into the variable
    # clientAddress. The variable clientAddress contains both the client’s IP address and the client’s port number.
    # Here, UDPServer will make use of this address information, as it provides a return address
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)  # This line attaches the client’s address (IP
    # address and port number) to the capital- ized message (after converting the string to bytes), and sends the
    # resulting packet into the server’s socket.
