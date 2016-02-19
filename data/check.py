import os
from data.game import Game as game
from data.profile import create, load


def loads():
    """Эта функция загружает данные профиля, и возвращыет значения"""
    lod = load()
    human = game(lod['name'], lod['many'])
    return human


def creates():
    """Эта функция принимает параметры и передает для создания профиля"""
    name_profile = input("Введите пожалуйста Ваше имя : ")
    many_profile = 1000
    create(name_profile, many_profile)


def start_game():
    """Эта фунция проверяет на существования уже профиля"""
    while True:
        if os.path.exists("save//profile.json"):
            choice = input("Вы желаете продолжить предведущую игру? y/n : ").upper()
            if choice == '' or choice == 'Y':
                return loads()
            elif choice == 'N':
                choice = input("Вы уверены?, пердведущий профиль будет утрачен навсегда y/n: ").upper()
                if choice == "Y" or choice == "":
                    creates()
                    return loads()
                elif choice == "N":
                    load()
        else:
            print("Предведущих сохранений не найдено")
            creates()
            return loads()