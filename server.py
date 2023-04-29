from socket import *
serverPort=12000
serverName='홍길동'
serverSocket=socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(100)
while True:
    connectionSocket,addr=serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print("Client of",sentence)
    connectionSocket.send(serverName.encode())
    connectionSocket.close()