from core_gui_tkinter.all import cards
from core_gui_tkinter.all import data
from core_gui_tkinter.profile import create
import sys
# from BlackJack_tkinter import main
# from tkinter import *


class Game(object):
    """Тут происходит самое действия игры"""

    def __init__(self, name, many):
        self.name = name  # Ваше имя
        self.many = many  # ваши деньги
        self.score = []  # тут считаются ваши очки с полученых карт
        self.cards = []  # тут сохраняются ваши карты
        self.bank = []  # тут сохраняются все ставки
        self.loss = []  # ну это сколько проиграли все(под вопросом о существовании)
        self.get_cards = cards()
        self.score_institutions = []
        self.card_institutions = []

    def restart(self):
        while True:
            create(self.name, self.many)    #сохраняется ваши результаты
            choice = input("Хотите сыграть еще ? 'y/n:' ").upper()
            # если хотите сыграть еще, то нужно очистить выданые вам карты и ваши очки
            if choice == "Y" or choice == "":
                if self.many == 0:
                    print("У Вас не достаточно денег для продолжения\n Досвидания!")
                    sys.exit()

                self.get_cards = cards()    #возвращает новый список карт
                self.score_institutions = []
                self.card_institutions = []
                self.cards = []
                self.score = []
                self.start()
            elif choice == "N":
                print("Удачи Вам, спасибо за игру")
                sys.exit()
            else:
                print("Я не знаю такой команды")

    def game(self):

        entry = Entry(main)  # сделали ставку или пропустили ставку
        btn1 = Button(main, text='OK')
        btn1.pack()

        if str(entry.get()) == "":
            rate = 0

        elif not entry.get().isdigit():
            print("Введите число ")
            return self.game()

        if self.many >= int(entry.get()):
            self.many -= int(entry.get())  # отняли вашу ставку от вашей суммы
            self.bank.append(int(entry.get()))  # додали эту сумму в банк
            # выдача карт и подсчет очков

            if not self.cards :     #при начале новой роздачи, выдают сначало 2 карты
                card = self.get_cards.pop()     #удаляет выбраную карту из колоды
                self.cards.append(card)
                self.score.append(data[card])
            card = self.get_cards.pop()     #удаляет выбраную карту из колоды
            self.cards.append(card)
            self.score.append(data[card])

        else:
            print("У Вас не достаточно денег")
            self.game()

        if sum(self.score) == 21:
            # если вы победили, то вся сумма из банка додается к вашей сумме
            self.bank.append(int(sum(self.bank) * 0.5))
            print("У Вас {0} очков".format(sum(self.score)))
            print("Вы победили, у Вас 21 очко, и выграли банк, в розмере {0}".format(sum(self.bank)))
            self.many += int(sum(self.bank))  # если Вы собрали ровно 21 то сумма в банке умножается в 50%
            self.bank = []  # банк пуст
            self.restart()
        elif sum(self.score) > 21:
            print("У Вас {0} очков".format(sum(self.score)))
            print("Вы проиграли, у Вас больше 21 очка")
            self.loss.append(sum(self.bank))
            self.bank = []
            self.restart()

        return """
####################
#### Игрок: {0}
#### Ваши карты: {1}
#### Ваши очки:  {2}
#### Ваши деньги:{3}
#### В банке:    {4}""".format(self.name, " ".join(self.cards), sum(self.score), self.many, sum(self.bank))

    def start(self):
        print(self.game())
        while True:
            choices = input("Хотите карту? 'y/n' : ").upper()
            if choices == "Y" or choices == "":
                print(self.game())
            elif choices == "N":
                if not self.bank != []:
                    sys.exit()
                else:
                    print(self.result())
                    print(self.restart())
            else:
                print("Пожалуста, введите нужною команду")

        self.result()

    def result(self):
        score_institutions = self.institutions()

        if int(sum(self.score)) > score_institutions:  # если у Вас больше чем у заведения
            self.bank.append(int(sum(self.bank) * 0.2))  # то выграш умножается на 20%
            self.many += int(sum(self.bank))
            print("У Вас {0} очков, заведения набрало {1} очков".format(sum(self.score), sum(self.score_institutions)))
            print("Вы победили, и вырали банк в розмере {0}".format(int(sum(self.bank))))
            self.bank = []
        elif int(sum(self.score)) < score_institutions:  # ну тут ясно что проиграли
            print("Вы проиграли, заведения набрало {0} ".format(score_institutions))
            print("У Вас {0} очков, заведения набрало {1} очков".format(sum(self.score), sum(self.score_institutions)))
            self.bank = []
        else:
            print("Ничья, нужно сиграть еще раз")  # если ничья
            self.cards = []
            self.score = []
            self.bank.append(int(sum(self.bank) * 0.5))  # банк автоматически умножается на 50% от суммы банка
            return self.start()  # игра запускается вновь
        return self.many, self.restart()

    def institutions(self):     #вот здесь играет заведение
        self.card_institutions = self.get_cards.pop()
        self.score_institutions.append(data[self.card_institutions])
        if sum(self.score_institutions) == sum(self.score):
            self.bank.append(50)
            return sum(self.score_institutions)
        elif sum(self.score_institutions) < sum(self.score):
            self.bank.append(50)
            self.institutions()
        if sum(self.score_institutions) > 21:
            return 0
        return sum(self.score_institutions)