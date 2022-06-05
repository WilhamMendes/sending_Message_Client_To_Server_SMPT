from base64 import decode
from socket import *

serverName = 'localhost'
serverPort = 2000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Input lowercase sentence: ')
clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode("utf-8"))
clientSocket.close()