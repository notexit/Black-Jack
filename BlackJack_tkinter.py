from tkinter import *
from core_gui_tkinter.menu import  menu
from core_gui_tkinter.all import greetings as greet


main = Tk()
main.geometry("400x400+40+40")
main.title("BlackJack")

label = Label(main, text=greet)
label.pack()

if __name__ == "__main__":

    menu(Menu, main, label, Button)
    main.mainloop()

    #start_menu()