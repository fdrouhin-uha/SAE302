import socket, sys 

HOST = 'localhost'
PORT = 10002

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socketClient.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")

while True:
    messageServeur = socketClient.recv(1024)
    print("S>", messageServeur)
    messageClient = input("C> ")
    socketClient.send(messageClient)

print("Connexion interrompue.")
socketClient.close()