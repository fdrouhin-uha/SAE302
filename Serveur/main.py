# exec
from socketClass import *
from commandeClass import *
from classtest import *
import threading
import time

def main():
    server = Supervision()
    server.execute()

if __name__ == '__main__':
    main()