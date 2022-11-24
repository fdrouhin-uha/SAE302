import socket

def main():
    # Create one client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 10002))
    print(f"C> Client connecté à {client.getpeername()}")
    client.send("Connecté".encode("utf-8"))
    data = client.recv(1024).decode("utf-8")
    print(data)

    while True:
        message = input("C> Entrez votre message: ") # Possible to send message to the server
        client.send(message.encode("utf-8"))
        data = client.recv(1024).decode("utf-8")
        print(data)
        if message == "exit": # Close the server when client send "exit" message
            client.close()
            print("C: Socket fermé")
            break
        elif message == "disconnect": # Close the client connection but not down the server if client send "close"
            print ("C: Client déconnecté")
            break
        elif message == "kill":
            print("C: Serveur éteint \n C: Client déconnecté \n C: Socket fermé \n C: Veuillez relancer le programme")
            break
        elif message == "reset":
            print("C: Serveur redémarré \n C: Client déconnecté \n C: Socket fermé \n C: Veuillez relancer le programme")
            break
        # DEBUG 
        # else:
        #     print(f"Message '{message}'envoyé")

def threading(process):
    import threading
    thread = threading.Thread(target=process)
    thread.start()


if __name__ == '__main__':
    main()
    #threading(main)