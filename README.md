# socket-programming-python
TCP and UDP socket programming including chat room application

## Solutions for the following problems:

1. Using UDP sockets in Python (files UDP_Server.py and UDP_Client.py). Make sure that you understand the purpose of UDP sockets, and the steps for creating and using these sockets. Run the Client and Server processes and observe the output.
2. Run the Client and the Server processes on different computers and check if they work as expected (you will need to specify the server’s IP address).
3. Design and implement a Client-Server system that uses UDP sockets to do the following:
  - The client sends the server a request. The request string can either be: “SEND_DATE” or “SEND_TIME”.
  - The server runs in a infinite loop where it keeps waiting for requests. Whenever it sees a request, it responds by sending either the current DATE or the current TIME in (HH:MM:SS) format as specified in the request.
  - When the Client receives a response, it prints it.
  - The Client runs in a loop where it generates multiple such requests, and the time between successive requests varies randomly between 1- 2 seconds. 
4. Using TCP sockets in Python (files TCP_Server.py and TCP_Client.py). Make sure that you understand the purpose of TCP sockets and the steps for
creating and using these sockets. Observe the differences between UDP and TCP sockets and the steps for their use. Run the TCP Client and Server
processes and observe the output.
5. Start the Wireshark and apply a filter such that only the traffic generated by your Client and Server processes is displayed. Identify the messages used by TCP during the Handshake and the actual text sent by the two processes. Are the “contents” of the packet (the message strings) visible within Wireshark?
(This is what we’d expect since the strings aren’t encrypted before sending.)
6. Design and implement a Client-Server system that uses TCP sockets in which the client initiates communication with a Server by sending the server it’s name.
