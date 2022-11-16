# exec
from socketClass import *
from commandeClass import *
import threading
import time

def main():
    # creating the socket
    s = SocketClass()
    # threading the socket
    start = time.perf_counter()
    t1 = threading.Thread(target=s.accept)
    end = time.perf_counter()   
    print(f"Finished in {round(end-start, 2)} second(s)")

if __name__ == '__main__':
    main()