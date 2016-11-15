#Nam Nguyen ID 49699153
#Randy Luong ID 43351454
import threading
from socket import *
import sys


buffer_size = 10000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 6789))
serverSocket.listen(1);

while True:
    print('Read to serve...');
    connectionSocket, addr = serverSocket.accept();
    try:
        
        message = connectionSocket.recv(buffer_size).decode(); #"data read" 4096 bytes for the buffer size
        filename = message.split()[1];
        #print(filename)
        f = open(filename[1:], "rb")                        

        outputdata = f.read();

        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n');
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i:i+1]);
        connectionSocket.send(b'\r\n\r\n');

        
        connectionSocket.close();
        
    except IOError:
        #Send response message for file not found
        connectionSocket.send('404 file not found');
        connectionSocket.close();

            
serverSocket.close();
sys.exit();
