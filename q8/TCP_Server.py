import socket 
import sys 
from _thread import *

localIP     = "127.0.0.1"
localPort   = 20001
BUF_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
server.bind((localIP, localPort)) 
server.listen(50) 
  
list_of_clients = [] 
client_addrs = []
name_dict = {}

def remove_connection(connection): 
    try:
        client_name = name_dict[connection]
        if connection in list_of_clients: 
            list_of_clients.remove(connection)
        conn.close()
    except Exception as e:
        print("Error in remove connection : {}".format(e))
        return

def remove_all():
    for connection in list_of_clients: 
        connection.close()
        list_of_clients.remove(connection)
        

def broadcast(message, connection): 
    try:
        if message == "":
            print("empty message from {}".format(connection))
            return
        print(message)
        for conn in list_of_clients: 
            if conn != connection: 
                try: 
                    conn.send(message.encode()) 
                except: 
                    print("Not able to broadcast message {} to {}".format(message, name_dict[conn]))
                    remove_connection(conn)
    except Exception as e:
        print("Error in broadcast : {}".format(e))
        return

def clientthread(conn, addr): 
    client_name = conn.recv(BUF_SIZE).decode('utf8')
    name_dict[conn] = client_name
    broadcast_message = "{} has joined. Member count = {}".format(client_name, len(list_of_clients))
    broadcast(broadcast_message, conn) 

    while True: 
        try: 
            message = conn.recv(BUF_SIZE).decode("utf8") 
            if message and message != "q": 
                message_to_send = "{}: {}".format(name_dict[conn], message) 
                broadcast(message_to_send, conn) 
            else: 
                conn.send(message.encode())
                remove_connection(conn)
                break 
        except Exception as e:
            print("Error in clientthread : {}".format(e) ) 
            sys.exit(0)
    
    broadcast_message = "{} has left. Member count = {}".format(client_name, len(list_of_clients))
    broadcast(broadcast_message, conn) 
print("********** CHAT ROOM MANAGER ************")        
try:  
    while True: 
        conn, addr = server.accept() 
        list_of_clients.append(conn) 
        client_addrs.append(addr)
        start_new_thread(clientthread,(conn,addr))    
except KeyboardInterrupt as msg:
    remove_all()
    print()
    server.close()
    print("Chat Room Manager closed successfully")
    sys.exit(0)
