import socket

class SocketClass():
    # creating the socket 
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(0)
        self.s.bind((socket.gethostname(), 10000))
        self.s.listen(5)

    def accept(self):
        while True:
            try:
                self.conn, self.addr = self.s.accept()
                print(f"Connection établie à {self.addr}")
                self.receive()
            except:
                pass
    
    def send(self, data):
        self.s.send(data)
        print("Data envoyée")

    def receive(self):
        self.data = self.conn.recv(1024)
        print(self.data)
        print("Data reçue")

    def close(self):
        self.s.close()
        print("Connection fermée")

    def connexion(self, serveur):
        self.s.connect((serveur, 10000))
        print(f"Connection établie à {serveur}")