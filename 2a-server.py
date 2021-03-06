
import socket

# parameters


def bind():
	server_socket=socket.socket()
	server_socket.bind((socket.gethostname(),1234))
	print('listening ...')
	server_socket.listen(1)
	c,addr = server_socket.accept()
	return c

def server_messages(c):
	while True:
		data=str(c.recv(1024).decode())
		data=data.lower()
		if data == "exit":
			print(data)
			c.send(str.encode("Server connection is closed"))
			
			break
		
		else:
			print(data)
			reply = 'Server Says: ' + data
			c.send(str.encode(reply))
	#c.close()
	
	
def main():
	c=bind()
	
	server_messages(c)
	
	c.close()

if __name__== "__main__":
	main()
