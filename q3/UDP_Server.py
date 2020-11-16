import socket
import sys
from datetime import datetime

def getTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def getDate():
    now = datetime.now()
    return now.strftime("%d-%m-%Y")

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_socket.bind((localIP, localPort))

print("UDP server up and listening")

try:
    while(True):
        message, address = server_socket.recvfrom(bufferSize)
        message = message.decode('utf8')
        
        if( message == "SEND_TIME"):
            server_response = getTime()
        elif( message == "SEND_DATE"):
            server_response = getDate()
        else:
            server_response = "Error in request format"
        server_response = server_response.encode()
        server_socket.sendto(server_response, address)
except KeyboardInterrupt as msg:
    server_socket.close()
    print("server socket closed successfully")
    sys.exit(0)