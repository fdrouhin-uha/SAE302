import socket
import threading
import platform
import os
import psutil
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10000))
server.listen(5)

 # Automatically accept the connection of many clients
def accept_clients():
    global client
    while True:
        global address
        global addr
        client, addr = server.accept()
        print('Connected to ', addr)
        threading.Thread(target=handle_client, args=(client,)).start()

 # Handle the client
def handle_client(client):
    data = client.recv(1024).decode("utf-8")
    print(f"S> Client {addr}, donnée {data}")
    while True:
        try:
            if data == "exit": # Close the connection when client send "exit" message
                server.close()
                print (f"S: Serveur fermé par {addr}")
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
                    mem = os.popen('free -t -m').readlines()
                    mem = mem[1].split()
                    client.send(str(mem[1]).encode("utf-8"))
                if platform.system() == "Linux":
                    mem = os.popen('free -t -m').readlines()
                    # get the second line, which contains the RAM data, and split it to an array where each data is an element
                    mem = mem[1].split()
                    # the 2nd element is the total RAM
                    client.send(str(mem[1]).encode("utf-8"))
                if platform.system() == "Mac":
                    # get the memory quantities to string
                    mem = os.popen('free -t -m').readlines()
                    # get the second line, which contains the RAM data, and split it to an array where each data is an element
                    mem = mem[1].split()
                    # the 2nd element is the total RAM
                    client.send(str(mem[1]).encode("utf-8"))
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
            if data == "":
                client.send("S: Message vide".encode("utf-8"))
        except BrokenPipeError:
            print("S: Client déconnecté")
            os.exit()
        except:            
            client.send("S: Commande non reconnue".encode("utf-8"))

def main():
    print('Server is running...')
    t1 = threading.Thread(target=accept_clients, args=[])
    t1.start()

if __name__ == '__main__':
    main()