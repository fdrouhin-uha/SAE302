# exec
from socketClass import *
from commandeClass import *

def main():
    # creating the socket
    s = SocketClass()
    # connection to the server
    s.connexion("192.168.0.50")

if __name__ == '__main__':
    main()