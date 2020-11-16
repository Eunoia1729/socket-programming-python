import socket                

#If localIP="", server will accept connections on all available IPv4 interfaces
localIP     = "127.0.0.1"
localPort   = 20002
BUF_SIZE  = 1024               

server_socket = None
try:
    server_socket = socket.socket(family = socket.AF_INET, 
    type = socket.SOCK_STREAM)          
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error {}".format(err))


server_socket.bind((localIP, localPort))         
print("socket binded to {}".format(localPort)) 
  
server_socket.listen(5)      
print("socket is listening")            

connection, address = server_socket.accept()      
with connection:
    print('Connected by', address)
    while True:
        client_response = connection.recv(BUF_SIZE).decode('utf8')
        if not client_response:
            break
        response_msg = "Message from Client : {}".format(client_response)
        print(response_msg)

        message = "Hi from server!"
        connection.sendall(message.encode()) 

server_socket.close()

        
# try:  
#     while True: 
    
#         client_socket, address = server_socket.accept()      
#         client_ip  = "Client IP Address:{}".format(address)
#         print(client_ip) 
        
#         # client_response = server_socket.recv(bufferSize).decode('utf8') 
#         # response_msg = "Message from Server : {}".format(client_response)
#         # print(response_msg)
#         # print()
        
#         message = "Hi from server!"
#         message = message.encode()
#         client_socket.sendall(message) 
#         client_socket.close() 
# except KeyboardInterrupt as msg:
#     server_socket.close()
#     print("Server socket closed successfully")
#     sys.exit(0)
    
