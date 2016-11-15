#Nam Nguyen ID 49699153
#Randy Luong ID 43351454
from threading import * 
from socket import *
import sys

buffer_size = 10000
j = 0;
threads = list();
serverSocket = socket(AF_INET, SOCK_STREAM)
def thread_listen():
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', 6789))
    serverSocket.listen(5);    

def handle_thread(outputdata, connectionSocket):
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i:i+1]);
    connectionSocket.send(b'\r\n\r\n');
    connectionSocket.close();

threads.append(Thread(target = thread_listen(), name = "MainThread"))
threads[j].start()
j+= 1;
while True:
    print('Read to serve...');
    if(threads[0].getName() == "MainThread"):
        connectionSocket, addr = serverSocket.accept();
        try:
            
            message = connectionSocket.recv(buffer_size).decode(); #"data read" 4096 bytes for the buffer size
            filename = message.split()[1];
            f = open(filename[1:], "rb")                        

            outputdata = f.read();

            #Send one HTTP header line into socket
            connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode());
            threads.append(Thread(target = handle_thread, args = (outputdata, connectionSocket), name = "Thread {}".format(j)))
            threads[j].deamon = True;
            threads[j].start();
            print("connection {}".format(j))
            j+= 1
            f.close();
        
            #Send the content of the requested file to the client
    ##        for i in range(0, len(outputdata)):           
    ##            connectionSocket.send(outputdata[i:i+1].encode());
            
            
        except IOError:
            #Send response message for file not found
            connectionSocket.send("404 file not found".encode());
            connectionSocket.close();

            
serverSocket.close();
sys.exit();
