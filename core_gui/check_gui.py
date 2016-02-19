import sys, os
from PyQt5.QtWidgets import QWidget,QMessageBox, QPushButton, QLineEdit, QInputDialog
from core_gui.profile_gui import create, load
from core_gui.game_core import Game as game


class Check_GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        while True:
            if os.path.exists("save//profile.json"):
                reply = QMessageBox.question(self, 'Внимания', "Вы желаете продолжить предведущую игру?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    return self.loads()
                elif reply == QMessageBox.No:
                    reply = QMessageBox.question(self, 'Внимания', "Вы уверены? \nВсе данные будут потеряные", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        self.creates()
                        return self.loads()
                    elif reply == QMessageBox.No:
                        return self.initUI()
            else:
                print("Предведущих сохранений не найдено")
                self.creates()
                return self.loads()

    def loads(self):
        """Эта функция загружает данные профиля, и возвращыет значения"""
        lod = load()
        human = game(lod['name'], lod['many'])
        return human


    def creates(self):
        text, ok = QInputDialog.getText(self, 'Создания', 'Введите Ваше имя:')
        many = 1000
        if ok:
            create(text, many)

