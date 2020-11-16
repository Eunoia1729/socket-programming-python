import socket

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
client_socket.sendto(bytesToSend, serverAddressPort)

server_response = client_socket.recvfrom(bufferSize)

msg = "Message from Server {}".format(server_response[0])
print(msg)