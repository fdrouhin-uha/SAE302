# GUI's class 

from PyQt6.QtWidgets import (QApplication,QHBoxLayout,QPushButton,QWidget,)

from commandeClass import *
from socketClass import *

class Gui():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Supervision")
    layout = QHBoxLayout()
    layout.addWidget(QPushButton("Left"))
    layout.addWidget(QPushButton("Center"))
    layout.addWidget(QPushButton("Right"))
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())