import socket                
import threading

serverIP     = "127.0.0.1"
serverPort   = 20001
BUF_SIZE  = 1024

def handle_messages(s):
    while 1:
        try:
            message = s.recv(BUF_SIZE).decode('utf8')
            if message == "q" or message == "":
                break
            print(message)
        except Exception as e:
            print("Error in handle_messages : {}".format(e))
            break

def handle_input(s, username):
    while 1:
        message = input()
        s.send(message.encode())
        if message == "q" or message == "":
            break

login_name = None
server_socket_address = (serverIP, serverPort) 

client_socket = None
try:
    client_socket = socket.socket(family = socket.AF_INET,
     type = socket.SOCK_STREAM)          
except socket.error as err:
    print("socket creation failed with error {}".format(err))

client_socket.connect(server_socket_address) 
login_name = input("Enter login name: ")
response_msg = "Welcome to the chatroom, {}!".format(login_name)
print(response_msg)    
client_socket.send(login_name.encode())
try:
    close_socket = 0
    message_handler = threading.Thread(target=handle_messages,args=(client_socket,))
    message_handler.start()

    input_handler = threading.Thread(target=handle_input,args=(client_socket, login_name,))
    input_handler.start()

    input_handler.join()
    message_handler.join()
except KeyboardInterrupt as ke:
    client_socket.close()
    print("Client closed successfully")
except Exception as e:
    print("Error : {}".format(e))
    client_socket.close()
else:
    client_socket.close()
    print("Chat window closed successfully")