from socket import *

serverName = 'localhost'
serverPort = 1998

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(10)

print('The server is ready to receive any massege in port: ', serverPort, "!")

while 10:
    connectionSocket, addr = serverSocket.accept()
    print('Conection to client adress: ', addr)
    connectionSocket.send(bytes('\nConnection established!', "utf-8"))

    confirmation_message = ('\n\nMessage received by the server and returned to the client! \n The message is: ')

    message_client_1 = connectionSocket.recv(1024).decode()
    capitalized_message_client_1 = message_client_1.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_1),  "utf-8"))

    message_client_2 = connectionSocket.recv(1024).decode()
    capitalized_message_client_2 = message_client_2.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_2),  "utf-8"))

    message_client_3 = connectionSocket.recv(1024).decode()
    capitalized_message_client_3 = message_client_3.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_3),  "utf-8"))

    message_client_4 = connectionSocket.recv(1024).decode()
    capitalized_message_client_4 = message_client_4.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_4),  "utf-8"))

    message_client_5 = connectionSocket.recv(1024).decode()
    capitalized_message_client_5 = message_client_5.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_5),  "utf-8"))

    message_client_6 = connectionSocket.recv(1024).decode()
    capitalized_message_client_6 = message_client_6.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_6),  "utf-8"))

    message_client_7 = connectionSocket.recv(1024).decode()
    capitalized_message_client_7 = message_client_7.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_7),  "utf-8"))

    message_client_8 = connectionSocket.recv(1024).decode()
    capitalized_message_client_8 = message_client_8.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_8),  "utf-8"))

    message_client_9 = connectionSocket.recv(1024).decode()
    capitalized_message_client_9 = message_client_9.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_9),  "utf-8"))

    message_client_10 = connectionSocket.recv(1024).decode()
    capitalized_message_client_10 = message_client_10.upper()
    connectionSocket.send(bytes('{}: {}' .format(confirmation_message, capitalized_message_client_10),  "utf-8"))

    connectionSocket.close()
