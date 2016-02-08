import sys
from data.game import Game as game

print("Приветствую, если хотите начать игру, введите Ваше имя")
name = input("Введите Ваше имя :")
human = game(name, 1000)


class Menu(object):
    """Меню игры"""

    @staticmethod
    def menu():
        while True:
            choice = input("Хотите начать инру? 'y/n '").upper()
            if choice == "Y":
                game.start(human)
            elif choice == "N":
                sys.exit()
            else:
                print("Пожалуста, введите нужною команду")
