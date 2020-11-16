import socket                
operators = ["+", "-", "/", "*"]

def isValidQuery(query):
    op_count = 0
    for op in operators:
        if op in query:
            op_count += 1
    return (op_count == 1)

def getOperator(query):
    for op in operators:
        if op in query:
            return op

def performQuery(query):
    op = getOperator(query)
    left, right = query.split(op)
    left.strip()
    right.strip()
    if( left == "" or right == ""):
        return "Warning: incorrect query format"
    left = float(left)
    right = float(right)
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "/":
        return left / right
    else:
        return left * right

def process_query(query):
    if query == "q":
        return "q"
    if (isValidQuery(query) == False):
        return "Warning: incorrect query format"
    return performQuery(query)

#If localIP="", server will accept connections on all available IPv4 interfaces
localIP     = "127.0.0.1"
localPort   = 20001
BUF_SIZE  = 1024               

server_socket = None
client_name = None
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

try:
    connection, address = server_socket.accept()    
    # print(connection)  
    with connection:
        client_name = connection.recv(BUF_SIZE).decode('utf8')
        response_msg = "Name of the client : {}".format(client_name)
        print(response_msg)
        
        print('Connected by', address)
        while True:
            client_request = connection.recv(BUF_SIZE).decode('utf8')
            if not client_request:
                break
            response_msg = "Message from {} : {}".format(client_name, client_request)
            print(response_msg)
            try:
                response = str(process_query(client_request))
            except ZeroDivisionError as err:
                response = "Invalid math operations"
            finally:    
                if response == "q":
                    break
                connection.send(response.encode()) 
except Exception as e:
    server_socket.close()
    print("error in connection : {}".format(e))
else:    
    server_socket.close()
    print("Session ended")