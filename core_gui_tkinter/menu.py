# -*- coding: utf-8 -*-

import sys
from core_gui_tkinter.game import Game as game
from core_gui_tkinter.help import help as helps
from core_gui_tkinter.check import start_game




def menu(Menu, main, label, Button):


    def game_start():
        label.destroy()
        start_game()

    def helpes():
        print(helps)

    def exit():
        print("Всего самого найлучшего")
        sys.exit()

    menus = Menu(main)
    main.config(menu=menus)

    filemenu = Menu(menus)
    menus.add_cascade(label="Game", menu=filemenu)
    filemenu.add_command(label="Start game", command=game_start)
    filemenu.add_command(label="Help...", command=helpes)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=exit)



