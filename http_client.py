#Nam Nguyen ID 49699153
#Randy Luong ID 43351454
from socket import *
import sys
import urllib.request
#The socket module forms the basis of all network communication

#Firstline specifies the address of the server. it can be an IP or servername. 
	#e.g. "128.138.32.126" or "yourserver.eng.uci.edu"
#second line shows which port your server will be working on(usually we use high number)

clientSocket = socket(AF_INET, SOCK_STREAM)
#this line creats a socket called clientSocket. 
#AF_INET specifies address family which is IPv4
#SOCK_STREAM shows the protocol for the socket which is TCP here.

clientSocket.connect((sys.argv[1], sys.argv[2]))
#initiates the TCP connection between the server and client. 3way handshake is established.


clientSocket.send(sys.argv[3])
#this linse sends the sentence through the client's socket into TCP connection.
#here we dont have to specify the address explicitly like UDP. 
#Instead we simply drop the packet to established TCP connection.
modifiedSentence = clientSocket.recv(10000)

#now when a message is recieved from internet to the client socket we will get it here.
#then we will put the message in modifiedMessage. 
#2048 here is the size of the buffer for receiving data

print ('From Server:', modifiedSentence.decode())
outputdata = urllib.request.urlopen(sys.argv[3]).read()
for i in range(0, len(outputdata)):
    print(outputdata[i:i+1]);
clientSocket.close()
#IMPORTANT TO RUN THIS CODE
#this code has to be run with arg parameters passed into through the command line
# client.py server_host server_port filename
#filename is the path to the file hosted on the server (e.g www.test.com/sam.html)
