import random
import sys
data = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10": 10,
    "J" : 2,
    "Q" : 3,
    "K" : 4,
    "A" : 11
}
cards = ["2", "3", "4", "5",
        "6", "7", "8","9","10",
        "J", "Q", "K", "A"]

class Player(object):       #походу клас не верно назван уже, после всех изменений и дополнений
    """Клас для создания всего"""

    def __init__(self, name, many):
        self.name = name    #Ваше имя
        self.many = many    #ваши деньги
        self.score = []     #тут считаются ваши очки с полученых карт
        self.cards = []     #тут сохраняются ваши карты
        self.bank = []      #тут сохраняются все ставки
        self.loss = []      #ну это сколько проиграли все(под вопросом о существовании)

    def name(self):
        return self.name, self.many

class Game(Player):
    """Тут происходит самое действия игры"""

    def restart(self):
        while True:
            choice = input("Хотите сыграть еще ? 'y/n: ").upper()
            #если хотите сыграть еще, то нужно очистить выданые вам карты и ваши очки
            if choice == "Y":
                self.cards = []
                self.score = []
                self.start()
            elif choice == "N":
                sys.exit()
            else:
                print("Я не знаю такой команды")

    def choice(self):
        rate = int(input("Ваша ставка: "))      #сделали ставку
        self.many -= rate       #отняли вашу ставку от вашей суммы
        self.bank.append(rate)  #додали эту сумму в банк
        #выдача карт и подсчет очков
        card = random.choice(cards)
        self.cards.append(card)
        self.score.append(data[card])

        if sum(self.score) == 21:
            #если вы победили, то вся сумма из банка додается к вашей сумме
            print("Вы победили, у Вас 21 очко")
            self.many += int(sum(self.bank))
            self.bank = []  #банк пуст
            self.restart()
        elif sum(self.score) > 21:
            print("Вы проиграли, у Вас больше 21 очка")
            self.loss.append(sum(self.bank))
            self.bank = []
            self.restart()
        return self.cards, sum(self.score), self.many

    def start(self):
        while True:

            choices = input("Хотите карту? 'y/n' : ").upper()
            if choices == "Y":
                print(self.choice())
            elif choices == "N":
                sys.exit()
            else:
                print("Пожалуста, введите нужною команду")

class Menu(Game):
    """Меню игры"""
    def menu(self):
        while True:
            i = input("Хотите начать инру? 'y/n '").upper()
            if i == "Y":
                self.start()
            elif i == "N":
                sys.exit()
            else:
                print("Пожалуста, введите нужною команду")
