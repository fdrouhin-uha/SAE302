import socket
import threading
import platform
import subprocess
import os
import time
import psutil
import cpuinfo
import sys



 # Automatically accept the connection of many clients
def accept_clients():
    global client
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 10000))
    server.listen(5)
    while True:
        global addr
        client, addr = server.accept()
        print('Connected to ', addr)
        threading.Thread(target=handle_client, args=(client,)).start()


 # Handle the client
def handle_client(client):
    threadAccept = threading.Thread(target=accept_clients)
    threadHandle = threading.Thread(target=handle_client, args=(client,))
    try:
        while True: 
            clientconnected = True
            if clientconnected == True:
                time.sleep(0.5)
                data = client.recv(1024).decode("utf-8")
                print(f"S> Client {addr}, donnée {data}")
                # execute this code when the server receives data from the client
                if data == "exit": # Close the connection when client send "exit" message
                    server.close()
                    print (f"S: Serveur fermé par {addr}")
                    break
                if data == "disconnect":  # Close the client connection but not the server if client send "close"
                    print("S: Client déconnecté")
                    client.close()
                    clientconnected = False 
                    print ("S: En attente du client...")
                    if clientconnected == False: # Wait for a new client to connect
                        # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        # server.bind(('localhost', 10000))
                        # server.listen(5)
                        # client, address = server.accept()
                        # print(f"S: Client {address} connecté")
                        threadAccept.start()
                        sys.exit(threadHandle)
                        client.send ("S: Connecté".encode("utf-8")  )
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
                        ramTotal = psutil.virtual_memory().total/1000000000
                        ramUsage = psutil.virtual_memory()[3]/1000000000
                        client.send(str(f"Ram disponible : {ramTotal} Go \nRam utilisée : {ramUsage} Go").encode("utf-8"))
                    if platform.system() == "Linux":
                        ramTotal = psutil.virtual_memory().total/1000000000
                        ramUsage = psutil.virtual_memory()[3]/1000000000
                        client.send(str(f"Ram disponible : {ramTotal} Go \nRam utilisée : {ramUsage} Go").encode("utf-8"))
                    if platform.system() == "Mac":
                        ramTotal = psutil.virtual_memory().total/1000000000
                        # get ram usage in bytes
                        ramUsage = psutil.virtual_memory()[3]/1000000000
                        client.send(str(f"Ram disponible : {ramTotal} Go \nRam utilisée : {ramUsage} Go").encode("utf-8"))
                if data == "cpu":
                    if platform.system() == "Windows" or platform.system() == "NT":
                        client.send(os.popen("wmic cpu get name").read().encode("utf-8"))
                    if platform.system() == "Linux":
                        client.send(cpuinfo.get_cpu_info()["brand_raw"].encode("utf-8"))
                    if platform.system() == "Mac":
                        client.send(os.popen("sysctl -n machdep.cpu.brand_string").read().encode("utf-8"))
                if data == "exit":
                    client.close()
                    print("S: Client déconnecté")
                    accept_clients()
                if data.startswith("dos:"):
                    try:
                        command = data.split(':')[1]
                        output = subprocess.check_output(command, shell=True)
                        client.send(output)
                    except Exception as e:
                        client.send(f"Erreur: {e}".encode('utf-8'))
                if data.startswith("linux:"):
                    try:
                        command = data.split(':')[1]
                        output = subprocess.check_output(command, shell=True)
                        client.send(output)
                    except Exception as e:
                        client.send(f"Erreur: {e}".encode('utf-8'))
            else:
                if clientconnected == False: # Wait for a new client to connect
                    # server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # server.bind(('localhost', 10000))
                    # server.listen(5)
                    # client, address = server.accept()
                    # print(f"S: Client {address} connecté")
                    threadAccept.start()
                    sys.exit(threadHandle)
                    client.send ("S: Connecté".encode("utf-8")  )
    except Exception as e:
        print(f"S: Erreur {e}")
        client.close()


def main():
    print('Server is running...')
    t1 = threading.Thread(target=accept_clients, args=[])
    t1.start()

if __name__ == '__main__':
    main()