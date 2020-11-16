import socket
import sys
import time, random
serverAddressPort   = ("127.0.0.1", 20001)
BUF_SIZE            = 1024
queries = ["SEND_DATE", "SEND_TIME"]

client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

try:
    while True:
        query_id = random.randint(0,1)
        query = queries[query_id]

        request_msg = "Message to Server : {}".format(query)
        print(request_msg)

        query = query.encode()
        client_socket.sendto(query, serverAddressPort)
        
        server_response = client_socket.recvfrom(BUF_SIZE)[0]
        server_response = server_response.decode('utf8')
        response_msg = "Message from Server : {}".format(server_response)
        print(response_msg)
        print()
        time.sleep(random.uniform(1,2))
except KeyboardInterrupt as msg:
    client_socket.close()
    print("client socket closed successfully")
    sys.exit(0)