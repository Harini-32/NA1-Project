import socket

ClientSocket = socket.socket()


print('Waiting for connection')
try:
    ClientSocket.connect((socket.gethostname(), 1234))
except socket.error as e:
    print(str(e))

#Response = ClientSocket.recv(1024)
#print(Response)
while True:
    Input = input('Say Something: ')
    if Input == "exit":
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024).decode()
        print(Response)
        if(Response == "Server connection is closed"):
            break
    else:
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))

ClientSocket.close()
