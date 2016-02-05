from data.core import cards
from data.core import data
import random
import sys


class Game(object):
    """Тут происходит самое действия игры"""

    def __init__(self, name, many):
        self.name = name  # Ваше имя
        self.many = many  # ваши деньги
        self.score = []  # тут считаются ваши очки с полученых карт
        self.cards = []  # тут сохраняются ваши карты
        self.bank = []  # тут сохраняются все ставки
        self.loss = []  # ну это сколько проиграли все(под вопросом о существовании)

    def restart(self):
        while True:
            choice = input("Хотите сыграть еще ? 'y/n: ").upper()
            # если хотите сыграть еще, то нужно очистить выданые вам карты и ваши очки
            if choice == "Y":
                self.cards = []
                self.score = []
                self.start()
            elif choice == "N":
                print("Удачи Вам, спасибо за игру")
                sys.exit()
            else:
                print("Я не знаю такой команды")

    def game(self):
        rate = input("Ваша ставка: 'c' - check ").upper()  # сделали ставку или пропустили ставку

        if self.many < 0:
            print("У вас не достаточно денег")
            self.game()
        if str(rate) == "C":
            rate = 0
        self.many -= int(rate)  # отняли вашу ставку от вашей суммы
        self.bank.append(int(rate))  # додали эту сумму в банк
        # выдача карт и подсчет очков
        card = random.choice(cards)
        self.cards.append(card)
        self.score.append(data[card])

        if sum(self.score) == 21:
            # если вы победили, то вся сумма из банка додается к вашей сумме
            print("Вы победили, у Вас 21 очко")
            self.many += int(sum(self.bank))
            self.bank = []  # банк пуст
            self.restart()
        elif sum(self.score) > 21:
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
        while self.many != 0:
            choices = input("Хотите карту? 'y/n' : ").upper()
            if choices == "Y":
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
        print("Тут будет победитель..в будущем")
        self.restart()
