from email import message
from socket import *


sender_email = input("Enter your email adress: ")
recived_email = input("Enter the email adress wil recived message: ")
msg = input("Enter the massage: ")
endmsg = "\r\n.\r\n"



# Choose a mail server (e.g. Google mail server) and call it mailserver
serverName = "localhost"
serverPort = 1998


# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#Fill in end


recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'Helo Alice!\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
 print('250 reply not received from server.')
 

# Send MAIL FROM command and print server response.
# Fill in start
mail_data = ("Mail From: <starwilliam7@hotmail.com>\r\n")
clientSocket.send(mail_data.encode())

recv_2 = clientSocket.recv(1024).decode()
print(recv_2)
# Fill in end



# Send RCPT TO command and print server response. 
# Fill in start
rctp_Data = ("RCPT TO: <mendeswil710@gmail.com>\r\n".encode())
clientSocket.send(rctp_Data)

recv_3 = clientSocket.recv(1024).decode()
print(recv_3)
# Fill in end



# Send DATA command and print server response. 
# Fill in start
data_command = "DATA\r\n".encode()
clientSocket.send(data_command)

recv_4 = clientSocket.recv(1024).decode()
print(recv_4)
# Fill in end



# Send message data.
# Fill in start
message_data = "Subject: {}\r\n" .format(msg).encode()
clientSocket.send(message_data)

recv_5 = clientSocket.recv(1024).decode()
print(recv_5)
# Fill in end



# Message ends with a single period.
# Fill in start
message_ends = "{}" .format(endmsg).encode()
clientSocket.send(message_ends)

recv_6 = clientSocket.recv(1024).decode()
print(recv_6)
# Fill in end


# Send QUIT command and get server response.
# Fill in start
quit_command = "QUIT\r\n".encode()
clientSocket.send(quit_command)

recv_7 = clientSocket.recv(1024).decode()
print(recv_7)

clientSocket.close()
# Fill in end
