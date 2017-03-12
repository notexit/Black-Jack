import os
from core_gui_tkinter.game import Game as game
from core_gui_tkinter.profile import create, load

from tkinter import Label, Entry, Button, Toplevel


def loads():
    """Эта функция загружает данные профиля, и возвращыет значения"""
    lod = load()
    human = game(lod['name'], lod['many'])
    return human


def creates():
    """Эта функция принимает параметры и передает для создания профиля"""
    main4 = Toplevel()
    def name_prof():
        create(entry.get(), many_profile)
        main4.destroy()

    label = Label(main4, text="You name : ")
    entry = Entry(main4)
    button = Button(main4, text="OK", command = name_prof)
    label.pack()
    entry.pack()
    button.pack()
    many_profile = 1000




def start_game():

    """Эта фунция проверяет на существования уже профиля"""


    def load():
        loads()
        main3.destroy()

    def creat():

        main2 = Toplevel()

        def yes():
            creates()
            loads()
            main2.destroy()

        def no():
            load()
            main3.destroy()
            main2.destroy()

        choice = Label(main2, text="Are you sure ?, the leading profile will be lost forever ")
        btn6 = Button(main2, text='YES', command = yes)
        btn7 = Button(main2, text='NO', command = no)
        choice.pack()
        btn6.pack()
        btn7.pack()



    if os.path.exists("save//profile.json"):


        main3 = Toplevel()
        choice = Label(main3,text="Do you wish to continue the game?")

        btn4 = Button(main3, text='YES', command = load)
        btn5 = Button(main3, text='NO', command = creat)

        choice.pack()
        btn4.pack()
        btn5.pack()



        # if choice == '' or choice == 'Y':
        #     return loads()
        # elif choice == 'N':
        #     choice = input("Вы уверены?, пердведущий профиль будет утрачен навсегда y/n: ").upper()
        #     if choice == "Y" or choice == "":
        #         creates()
        #         return loads()
        #     elif choice == "N":
        #         load()
    else:
        print("No presets saved")
        creates()
        return loads()