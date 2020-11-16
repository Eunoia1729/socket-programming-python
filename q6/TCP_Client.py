import socket                

serverIP     = "127.0.0.1"
serverPort   = 20001
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
client_name = input("Enter name: ")
client_socket.send(client_name.encode())

while True:
    query = input("Enter query: ")
    client_socket.send(query.encode())

    server_response = client_socket.recv(BUF_SIZE).decode('utf8') 
    response_msg = "Message from Server : {}".format(server_response)
    response_msg.strip()
    if not server_response:
        break
    print(response_msg)
    print()

client_socket.close()        
print("Client closed socket succefully")