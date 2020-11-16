import socket

localIP     = ""
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
server_socket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    client_response = server_socket.recvfrom(bufferSize)
    message = client_response[0]
    address = client_response[1]

    client_message = "Message from Client:{}".format(message)
    client_ip  = "Client IP Address:{}".format(address)
    
    print(client_message)
    print(client_ip)

    # Sending a reply to client
    server_socket.sendto(bytesToSend, address)
