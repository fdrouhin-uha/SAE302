# exec
from socketClass import *
from commandeClass import *

def main():
    # creating the socket
    s = SocketClass()
    # creating the commands
    CommandeClass.CPU(s)
    CommandeClass.IP(s)
    CommandeClass.HOST(s)
    CommandeClass.OS(s)
    CommandeClass.RAM(s)

if __name__ == '__main__':
    main()