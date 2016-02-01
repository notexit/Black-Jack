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

class Game(object):
	my_cards = []
	my_score = []
	def __init__(self):
		self.my_cards
		self.my_score

	def choice(self):
		card = random.choice(cards)
		self.my_cards.append(card)
		self.my_score.append(data[card])
		if sum(self.my_score) == 21:
			print("Вы победили, у Вас 21 очко")
			sys.exit()
		elif sum(self.my_score) > 21:
			print("Вы проиграли, у Вас больше 21 очка")
			sys.exit()
		return self.my_cards, sum(self.my_score)