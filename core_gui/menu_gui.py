import sys
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from core_gui.help_gui import Help_GUI
from core_gui.check_gui import Check_GUI as check
from core_gui.game_gui import BlackJackGUI as games

class Menu_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.start_menu()

    def start_menu(self):
        lbl1 = QLabel('Menu', self)
        lbl1.move(100, 10)

        start_btn = QPushButton('START', self)
        start_btn.setToolTip('Эта кнопка для <b>СТАРТА</b> игры')
        start_btn.clicked.connect(self.start)
        start_btn.resize(start_btn.sizeHint())
        start_btn.move(75, 40)

        help_btn = QPushButton('HELP', self)
        help_btn.setToolTip('Это кнопка получения <b>ПОМОЩИ</b>')
        help_btn.clicked.connect(self.help)
        help_btn.resize(help_btn.sizeHint())
        help_btn.move(75, 80)

        exit_btn = QPushButton('EXIT', self)
        exit_btn.setToolTip('Это кнопка для <b>ВЫХОДА</b>')
        exit_btn.clicked.connect(QCoreApplication.instance().quit)
        exit_btn.resize(exit_btn.sizeHint())
        exit_btn.move(75, 120)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Menu')
        self.show()

    def start(self):
        w = check()
        q = games(w.loads().name, w.loads().many)
        q.exec_()


    def help(self):
        h = Help_GUI()
        h.exec_()

    def exit(self):
        pass



def start_menu():
    app = QApplication(sys.argv)
    ex = Menu_GUI()
    sys.exit(app.exec_())