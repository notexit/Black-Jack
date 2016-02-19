import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from core_gui.game_gui import BlackJackGUI

class Help_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.start_menu()

    def start_menu(self):
        lbl1 = QLabel('Help', self)
        lbl1.move(100, 10)

        exit_btn = QPushButton('EXIT', self)
        exit_btn.setToolTip('Это кнопка для <b>ВЫХОДА</b>')
        exit_btn.clicked.connect(QCoreApplication.instance().quit)
        exit_btn.resize(exit_btn.sizeHint())
        exit_btn.move(75, 120)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menu')
        self.show()
