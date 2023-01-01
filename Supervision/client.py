import sys
import socket
import os
import platform
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.valeurConnection = "Déconnecté"

        labelConnect = QLabel("Adresse IP :")
        self.textConnect = QLineEdit("127.0.0.1")
        labelPort = QLabel("Port :")
        self.textPort = QLineEdit("10000")
        boutonConnect = QPushButton("Connexion")
        labelStatus = QLabel("Status :")
        self.statusConnection = QLabel(f"{self.valeurConnection}")
        boutonDeconnection = QPushButton("Déconnexion")

        self.HOST = str(self.textConnect.text())
        self.PORT = int(self.textPort.text())

        grid.addWidget(labelConnect, 0, 0)
        grid.addWidget(self.textConnect, 0, 1)
        grid.addWidget(labelPort,0 ,2)
        grid.addWidget(self.textPort, 0, 3)
        grid.addWidget(boutonConnect, 1, 0, 1, 2)
        grid.addWidget(labelStatus, 2, 0)
        grid.addWidget(self.statusConnection, 2, 1, 1, 3)
        grid.addWidget(boutonDeconnection, 1, 2, 1, 2)

        # t1 = threading.Thread(target=self.__actionConnect).start()
        # boutonConnect.clicked.connect(t1)
        boutonConnect.clicked.connect(self.__actionConnect)
        boutonDeconnection.clicked.connect(self.__actionDeconnect)

    def __actionConnect(self):
        try:
            #threading.Thread(target=self.__actionConnect).start()
            self.HOST = str(self.textConnect.text())
            self.PORT = int(self.textPort.text())
            self.client.connect((self.HOST, self.PORT))
            self.valeurConnection = "Connecté"
            self.statusConnection.setText(f"{self.valeurConnection}")
            print("Connecté")
            self.shell = Shell()
            self.shell.show()
        except ConnectionRefusedError:
            self.valeurConnection = "Connexion refusée (port ou adresse IP incorrect / ConnectionRefusedError)"
            self.statusConnection.setText(f"{self.valeurConnection}")
            print("Connexion refusée (port ou adresse IP incorrect)")
        except ConnectionResetError:
            self.valeurConnection = "Connexion perdue (serveur fermé)"
            self.statusConnection.setText(f"{self.valeurConnection}")
            print("Connexion perdue (serveur fermé)")
        except ConnectionAbortedError:
            self.valeurConnection = "Connexion interrompue"
            self.statusConnection.setText(f"{self.valeurConnection}")
            print("Connexion interrompue")
        except BrokenPipeError:
            self.valeurConnection = "Connexion interrompue (BrokenPipeError)"
            self.statusConnection.setText(f"{self.valeurConnection}")
            print("Connexion interrompue (BrokenPipeError)")
        except ValueError:
            self.valeurConnection = "Valeur invalide (port ou adresse IP incorrect)"
            self.statusConnection.setText(f"{self.valeurConnection}")
            print("Valeur invalide (port ou adresse IP incorrect)")
        # except OSError:
        #     self.valeurConnection = "Impossible de se connecter (OSErr)"
        #     self.statusConnection.setText(f"{self.valeurConnection}")
        #     print("OSError")

    def __actionDeconnect(self):
        self.client.send("disconnect".encode("utf-8"))
        self.client.close()
        self.valeurConnection = "Déconnecté"
        self.statusConnection.setText(f"{self.valeurConnection}")
        print("Déconnecté")
        sys.exit(threading.Thread(target=self.__actionConnect))

    def getHOST(self):
        return self.HOST

    def getPORT(self):
        return self.PORT

    def getClient(self):
        return self.client

class Shell(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.resultatCommande = "En attente de commande"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = MainWindow().getHOST()
        self.PORT = MainWindow().getPORT()
        self.client.connect((self.HOST, self.PORT))

        boutonRam = QPushButton("RAM")
        boutonCPU = QPushButton("CPU")
        boutonOS = QPushButton("OS")
        boutonHOST = QPushButton("HOST")
        boutonShutdonw = QPushButton("Shutdown")
        boutonReboot = QPushButton("Reboot")
        boutonExit = QPushButton("Exit")
        self.retourShell = QTextEdit(f"{self.resultatCommande}")
        self.retourShell.setReadOnly(True)
        labInput = QLabel("Commande :")
        self.inputShell = QLineEdit("")
        boutonSend = QPushButton("Envoyer")

        grid.addWidget(boutonRam, 0, 0)
        grid.addWidget(boutonCPU, 0, 1)
        grid.addWidget(boutonOS, 0, 2)
        grid.addWidget(boutonHOST, 0, 3)
        grid.addWidget(boutonShutdonw, 0, 4)
        grid.addWidget(boutonReboot, 0, 5)
        grid.addWidget(boutonExit, 0, 6)
        grid.addWidget(self.retourShell, 1, 0, 6, 4)
        grid.addWidget(labInput, 7, 0)
        grid.addWidget(self.inputShell, 7, 1, 1, 3)
        grid.addWidget(boutonSend, 7, 4)

        boutonRam.clicked.connect(self.__actionRam)
        boutonExit.clicked.connect(self.__actionExit)
        boutonSend.clicked.connect(self.__actionSend)
        boutonOS.clicked.connect(self.__actionOS)
        boutonCPU.clicked.connect(self.__actionCPU)
        boutonHOST.clicked.connect(self.__actionHOST)
        boutonShutdonw.clicked.connect(self.__actionShutdown)
        boutonReboot.clicked.connect(self.__actionReboot)

    def __actionSend(self):
        message = platform.system().lower()+':'+self.inputShell.text().lower()
        self.client.send(message.encode())
        self.resultatCommande = self.client.recv(1024).decode()
        self.retourShell.setText(f"{self.resultatCommande}")

    def __actionRam(self):
        self.client.send('ram'.encode('utf-8'))
        self.resultatCommande = self.client.recv(1024).decode('utf-8')
        self.retourShell.setText(f"{self.resultatCommande}")
        print(self.resultatCommande)

    def __actionOS(self):
        self.client.send('os'.encode('utf-8'))
        self.resultatCommande = self.client.recv(1024).decode('utf-8')
        self.retourShell.setText(f"{self.resultatCommande}")
        print(self.resultatCommande)

    def __actionCPU(self):
        self.client.send('cpu'.encode('utf-8'))
        self.resultatCommande = self.client.recv(1024).decode('utf-8')
        self.retourShell.setText(f"{self.resultatCommande}")
        print(self.resultatCommande)

    def __actionHOST(self):
        self.client.send('hostname'.encode('utf-8'))
        self.resultatCommande = self.client.recv(1024).decode('utf-8')
        self.retourShell.setText(f"{self.resultatCommande}")
        print(self.resultatCommande)
        
    def __actionShutdown(self):
        self.client.send('kill'.encode('utf-8'))
        self.resultatCommande = self.client.recv(1024).decode('utf-8')
        self.retourShell.setText(f"{self.resultatCommande}")
        print(self.resultatCommande)

    def __actionReboot(self):
        self.client.send('reset'.encode('utf-8'))
        self.resultatCommande = self.client.recv(1024).decode('utf-8')
        self.retourShell.setText(f"{self.resultatCommande}")
        print(self.resultatCommande)

    def __actionExit(self):
        self.client.send('exit'.encode('utf-8'))
        self.client.close()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()

    app.exec()
