import sys
from data.game import Game as game
from data.profile import Profile

profil = Profile()

print("Приветствую, если хотите начать игру, создайте новый профиль")

name = profil.name()

human = game(name[0], name[1])

print(human.name)


class Menu(object):
    """Меню игры"""
    @staticmethod
    def menu():
        while True:
            choice = input("Хотите начать игру? 'y/n '").upper()
            if choice == "Y" or choice == "":
                game.start(human)
            elif choice == "N":
                print("Всего самого найлучшего")
                sys.exit()
            else:
                print("Пожалуйста, введите нужною команду")
