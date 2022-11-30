import socket
import os
import platform

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10000))
server.listen(5)
print("S: Server is listening...")
clientconnected = False
print("S: Waiting for client...")


# Wait for a client to connect
while clientconnected == False:
    client, address = server.accept()
    print(f"S> Client connecté {address}")
    clientconnected = True
    client.send("S: Connecté".encode("utf-8"))

# Receive data from the client when client connected
while clientconnected == True:
    data = client.recv(1024).decode("utf-8")
    print(f"S> Client {address}, donnée {data}")
    try:
        if data == "exit": # Close the connection when client send "exit" message
            server.close()
            print (f"S: Serveur fermé par {address}")
            break
        if data == "disconnect":  # Close the client connection but not the server if client send "close"
            print("S: Client déconnecté")
            client.close()
            clientconnected = False 
            print ("S: En attente du client...")
            while clientconnected == False: # Wait for a new client to connect
                client, address = server.accept()
                print(f"S: Client {address} connecté")
                clientconnected = True
                client.send ("S: Connecté".encode("utf-8"))
        if data == "kill":
            if platform.system() == "Windows":
                os.system("shutdown /s /t 1")
            if platform.system() == "Linux":
                os.system("shutdown -h now")
            if platform.system() == "Mac":
                os.system("shutdown -h now")
            else:
                print("S: OS non supporté")
        if data == "reset":
            if platform.system() == "Windows":
                os.system("shutdown /r /t 1")
            if platform.system() == "Linux":
                os.system("reboot")
            if platform.system() == "Mac":
                os.system("reboot")
            else:
                print("S: OS non supporté")
        if data == "os":
            client.send(platform.system().encode("utf-8"))
        if data == "ip":
            client.send(socket.gethostbyname(socket.gethostname()).encode("utf-8"))
        if data == "hostname":
            client.send(socket.gethostname().encode("utf-8"))
        if data == "ram":
            if platform.system() == "Windows":
                client.send(os.popen("wmic memorychip get capacity").read().encode("utf-8"))
            if platform.system() == "Linux":
                client.sendall(os.popen("cat /proc/meminfo").read().encode("utf-8"))
            if platform.system() == "Mac":
                client.send(os.popen("sysctl hw.memsize").read().encode("utf-8"))
            else:
                print("S: OS non supporté")
        if data == "cpu":
            if platform.system() == "Windows":
                client.send(os.popen("wmic cpu get name").read().encode("utf-8"))
            if platform.system() == "Linux":
                client.sendall(os.popen("cat /proc/cpuinfo").read().encode("utf-8"))
            if platform.system() == "Mac":
                client.send(os.popen("sysctl -n machdep.cpu.brand_string").read().encode("utf-8"))
            else:
                print("S: OS non supporté")
        if data != "exit" or data != "disconnect" or data != "kill" or data != "reset" or data != "os" or data != "ip" or data != "hostname" or data != "ram" or data != "cpu": 
            client.send("S: Message non reconnue".encode("utf-8"))
        if data == "":
            client.send("S: Message vide".encode("utf-8"))
    except BrokenPipeError:
        print("S: Client déconnecté")
        break
    except:            
        client.send("S: Commande non reconnue".encode("utf-8"))

if __name__ == '__main__':
    pass