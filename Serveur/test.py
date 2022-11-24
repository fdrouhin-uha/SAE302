import socket, sys

HOST = 'localhost'
PORT = 10002

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socketServer.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while True:
    print("Serveur prêt, en attente de requêtes ...")
    socketServer.listen(5)
    connexion, adresse = socketServer.accept()
    print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
    connexion.send("Vous êtes connecté au serveur. Envoyez des messages.")
    messageClient = connexion.recv(1024)
    while True:
        print("C>", messageClient)
        if messageClient.upper() == "FIN" or messageClient =="":
            break
        messageServeur = input("S> ")
        connexion.send(messageServeur)
        messageClient = connexion.recv(1024)

    connexion.send("Au revoir !")
    print("Connexion interrompue.")
    connexion.close()

    ch = input("Fermer le serveur ? O/N ")
    if ch.upper() == "O":
        break