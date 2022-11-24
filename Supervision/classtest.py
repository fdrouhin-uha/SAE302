import socket

class Supervision():
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Create one client socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 10000))
        print(f"Client conncté à {client.getpeername()}")
        client.send("Connecté".encode())
        data = client.recv(1024).decode()
        print(data)

    def execute(self):
        while True:
            message = input("Entrez votre message: ") # Possible to send message to the server
            self.send(message.encode())
            if message == "exit": # Close the server when client send "exit" message
                self.close()
                break
            elif message == "bye": # Close the client connection but not down the server if client send "close"
                print ("Client déconnecté")
                break