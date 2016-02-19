import sys
from data.game import Game as game
from data.help import help as helps
from data.check import start_game


class Menu(object):
    """Меню игры"""

    @staticmethod
    def menu():
        while True:
            print("Хотите начать игру? ")
            choice = input("--->>>  ")
            if choice == "1":
                game.start(start_game())
            elif choice == "2":
                print(helps)
            elif choice == "3":
                print("Всего самого найлучшего")
                sys.exit()
            else:
                print("Пожалуйста, введите нужною команду")
