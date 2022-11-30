import socket
import logging

def main():
    # Create one client socket
    global HOST
    global PORT
    global client
    HOST = str(input("C> IP: "))
    PORT = int(input("C> Port: "))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print(f"C> Client connecté à {client.getpeername()}")
    client.send("Connecté".encode("utf-8"))
    data = client.recv(1024).decode("utf-8")
    print(data)

    # while True:
    #     try:
    #         message = input("C> Entrez votre message: ") # Possible to send message to the server
    #         client.send(message.encode("utf-8"))
    #         data = client.recv(1024).decode("utf-8")
    #         print(data)
    #         if message == "exit": # Close the server when client send "exit" message
    #             client.close()
    #             print("C: Socket fermé")
    #             break
    #         elif message == "disconnect": # Close the client connection but not down the server if client send "close"
    #             print ("C: Client déconnecté")
    #             break
    #         elif message == "kill":
    #             print("C: Serveur éteint \n C: Client déconnecté \n C: Socket fermé \n C: Veuillez relancer le programme")
    #             break
    #         elif message == "reset":
    #             print("C: Serveur redémarré \n C: Client déconnecté \n C: Socket fermé \n C: Veuillez relancer le programme")
    #             break

    #         # log as csv with logging module
    #         # log time, message, data, ip, port
    #         logging.basicConfig(filename="log.csv", level=logging.INFO, format="%(asctime)s,%(message)s,%(data)s,%(ip)s,%(port)s")
    #         logging.info(message, extra={"data": data, "ip": client.getpeername()[0], "port": client.getpeername()[1]})
            
                
    #     except KeyboardInterrupt:
    #         print("Système: Message d'intéruption reçu \nC: Client déconnecté")
    #         break
    #     except ConnectionAbortedError:
    #         print("Système: Erreur de connection \nC: Serveur déconnecté")
    #         break
    #     except ConnectionResetError:
    #         print("Système: Connection réinitialisé \nC: Serveur déconnecté")
    #         break
    #     # DEBUG 
    #     # else:
    #     #     print(f"Message '{message}'envoyé")

def get_data():
    while True:
        data = client.recv(1024).decode("utf-8")
        print(data)

def send():
    while True:
        message = input("C> Entrez votre message: ") # Possible to send message to the server
        client.send(message.encode("utf-8"))
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

def threading(process):
    import threading
    thread = threading.Thread(target=process)
    thread.start()


if __name__ == '__main__':
    threading(main())
    threading(get_data())
    threading(send())