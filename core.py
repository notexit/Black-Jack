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

class Player(object):
	"""Клас для создания игрока"""

	def __init__(self, name, many, score, cards):
		self.name = name
		self.many = many
		self.score = []
		self.cards = []

	def name(self):
		return self.name, self.many

class Game(Player):
	"""Тут происходит самое действия игры"""

	def choice(self):
		rate = int(input("Ваша ставка: "))
		self.many = self.many - rate
		card = random.choice(cards)
		self.cards.append(card)
		self.score.append(data[card])

		if sum(self.score) == 21:
			print("Вы победили, у Вас 21 очко")
			sys.exit()
		elif sum(self.score) > 21:
			print("Вы проиграли, у Вас больше 21 очка")
			sys.exit()
		return self.cards, sum(self.score), self.many