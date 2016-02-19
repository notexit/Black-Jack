import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QGridLayout, QLabel, QDesktopWidget, QLineEdit, QApplication)
from PyQt5.QtCore import QCoreApplication
from core_gui.all_gui import cards, data
from core_gui.profile_gui import create



class BlackJackGUI(QWidget):
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

        super().__init__()
        self.start_gui()

    def start_gui(self):

        self.btn_quit = QPushButton('Quit', self)
        self.btn_quit.setToolTip('Это кнопка <b>Выход</b>')
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_quit.resize(self.btn_quit.sizeHint())
        self.btn_quit.move(20, 250)

        self.btn_rate = QPushButton('ставка', self)
        self.btn_rate.setToolTip('Когда вы ввели ставку, этой кнопкой вы подтверждаете ввод <b>ставка</b>')
        self.btn_rate.clicked.connect(self.core)
        self.btn_rate.resize(self.btn_rate.sizeHint())
        self.btn_rate.move(240, 200)

        self.enough_btn = QPushButton('хватит', self)
        self.enough_btn.setToolTip('Эта кнопка для остановки роздачи Ваших карт <b>хватит</b>')
        self.enough_btn.clicked.connect(QCoreApplication.instance().quit)
        self.enough_btn.resize(self.enough_btn.sizeHint())
        self.enough_btn.move(290, 250)

        self.cards_btn = QPushButton('карту', self)
        self.cards_btn.setToolTip('Эта кнопка для получения еще одной карты <b>карту</b>')
        self.cards_btn.clicked.connect(QCoreApplication.instance().quit)
        self.cards_btn.resize(self.cards_btn.sizeHint())
        self.cards_btn.move(190, 250)

        self.chkbtn = QPushButton('check', self)
        self.chkbtn.setToolTip('Это кнопка для пропуска ставки <b>check</b>')
        self.chkbtn.clicked.connect(QCoreApplication.instance().quit)
        self.chkbtn.resize(self.chkbtn.sizeHint())
        self.chkbtn.move(330, 200)

        self.lblsum = QLabel('сумма ставки', self)
        self.lblsum.move(130, 220)

        self.lblyou_many = QLabel('ваши деньги', self)
        self.lblyou_many.move(10, 220)

        self.lblmany = QLabel(str(self.many), self)
        self.lblmany.move(30, 200)

        self.lblname = QLabel(self.name, self)
        self.lblname.move(40, 120)

        self.lblname_cards = QLabel('карты', self)
        self.lblname_cards.move(20, 150)

        self.lblcards = QLabel(" ".join(self.cards), self)
        self.lblcards.move(90, 150)

        self.lblname_score = QLabel('очки', self)
        self.lblname_score.move(20, 170)

        self.lblscore = QLabel(str(sum(self.score)), self)
        self.lblscore.move(90, 170)

        self.lblname_bank = QLabel('банк', self)
        self.lblname_bank.move(220, 110)

        self.lblbank = QLabel(str(self.bank), self)
        self.lblbank.move(270, 110)

        self.lblinst_name = QLabel('instituties', self)
        self.lblinst_name.move(30, 10)

        self.lblinst_name_cards = QLabel('карты', self)
        self.lblinst_name_cards.move(20, 50)

        self.lblinst_cards = QLabel('cards_inst', self)
        self.lblinst_cards.move(80, 50)

        self.lblinst_name_score = QLabel('очки', self)
        self.lblinst_name_score.move(20, 70)

        self.lblinst_score = QLabel('score_inst', self)
        self.lblinst_score.move(80, 70)

        self.lbl_info = QLabel('info', self)
        self.lbl_info.move(200, 160)

        self.lineEdit = QLineEdit(str(50), self)
        self.lineEdit.move(110, 200)

        self.setGeometry(400, 200, 420, 290)
        self.setWindowTitle('BlackJackGUI')
        self.show()

    def core(self):

        rate = 50#self.lineEdit()

        if str(rate) == "":
            rate = 0

        # elif not rate.isdigit():
        #     print("Введите число ")
        #     return self.game()

        if self.many >= int(rate):
            self.many -= int(rate)  # отняли вашу ставку от вашей суммы
            self.bank.append(int(rate))  # додали эту сумму в банк
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
            #self.loss.append(sum(self.bank))
            self.bank = []
            self.restart()

        return self.name, " ".join(self.cards), sum(self.score), self.many, sum(self.bank)

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