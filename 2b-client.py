import socket

# parameters

def client_messages(filename,client_socket):
        
	while True:
		if filename == "exit":
			client_socket.send(str.encode(filename))
			data=str(client_socket.recv(1024).decode())
			print(data)
			if(data == "Client connection is closed"):
				break
		

		
		else:
			client_socket.send(str.encode(filename))
			data=str(client_socket.recv(1024).decode())
			print(data)
			filename=input("Enter standard messages -->")
			filename=filename.lower()

def main():
	client_socket=socket.socket()
	client_socket.connect((socket.gethostname(),1234))
	filename=input("Enter message here -->")
	filename=filename.lower()
	client_messages(filename,client_socket)
	client_socket.close()

if __name__== "__main__":
	main()
