import os
import sys
import platform
import socket

class CommandeClass():
    def Disconnect(self):
        self.s.close()
        print ("Vous avez été déconnecté")

    def Kill(self):
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        if platform.system() == "Linux":
            os.system("shutdown -h now")
        if platform.system() == "Mac":
            os.system("shutdown -h now")
        else:
            print("OS non supporté")

    def Reset(self):
        if platform.system() == "Windows":
            os.system("shutdown /r /t 1")
        if platform.system() == "Linux":
            os.system("reboot")
        if platform.system() == "Mac":
            os.system("reboot")
        else:
            print("OS non supporté")

    def OS(self):
        print(f"OS: {platform.system()}")

    def RAM(self):
        print(f"RAM : {str(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES'))}")

    def CPU(self):
        print("CPU: " + platform.processor())

    def IP(self):
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)
        print(f"IP: {IPAddr}")

    def HOST(self):
        print(f"HOST: {socket.gethostname()}")