# exec
from socketClass import *
from commandeClass import *
from gui import *

def main():
    # creating the socket
    s = SocketClass()
    # connection to the server
    s.connexion("192.168.0.50")

    Gui()

if __name__ == '__main__':
    main()