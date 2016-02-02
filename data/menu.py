import sys
from data.game import Game as game

human = game("Yurii", 1000)

class Menu(object):
    """Меню игры"""

    @staticmethod
    def menu():
        while True:
            i = input("Хотите начать инру? 'y/n '").upper()
            if i == "Y":
               game.start(human)
            elif i == "N":
                sys.exit()
            else:
                print("Пожалуста, введите нужною команду")