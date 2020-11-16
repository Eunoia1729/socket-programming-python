import socket                

serverIP     = "127.0.0.1"
serverPort   = 20002
BUF_SIZE  = 1024
server_socket_address = (serverIP, serverPort) 

client_socket = None
try:
    client_socket = socket.socket(family = socket.AF_INET,
     type = socket.SOCK_STREAM)          
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error {}".format(err))

client_socket.connect(server_socket_address) 

message = "Hi from client !"
message = message.encode()
client_socket.sendto(message, server_socket_address)

server_response = client_socket.recv(BUF_SIZE).decode('utf8') 
response_msg = "Message from Server : {}".format(server_response)
print(response_msg)
    
client_socket.close()        
