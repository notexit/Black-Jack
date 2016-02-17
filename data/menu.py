import sys, os
from data.game import Game as game
from data.profile import create, load


class Menu(object):
    """Меню игры"""

    @staticmethod
    def menu():
        while True:
            choice = input("Хотите начать игру? 'y/n '").upper()
            if choice == "Y" or choice == "":
                game.start(loads())
            elif choice == "N":
                print("Всего самого найлучшего")
                sys.exit()
            else:
                print("Пожалуйста, введите нужною команду")


print("Приветствую, если хотите начать игру, создайте новый профиль или загрузите предведущую")


def loads():
    lod = load()
    human = game(lod['name'], lod['many'])
    return human


def creates():
    name_profile = input("Введите пожалуйста Ваше имя : ")
    many_profile = 1000
    create(name_profile, many_profile)


while True:
    if os.path.exists("profile.json"):
        choice = input("Вы желаете продолжить предведущую игру? y/n : ").upper()
        if choice == '' or choice == 'Y':
            Menu.menu()
        elif choice == 'N':
            creates()
            Menu.menu()
    else:
        print("Предведущих сохранений не найдено")
        creates()
        Menu.menu()
