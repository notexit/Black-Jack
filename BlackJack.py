from core import *

game = Game("Human", 1000, [], [])

def start():
	while True:

		choices = input("Хотите карту? 'y/n' : ").upper()
		if choices == "Y":
			print(game.choice())
		elif choices == "N":
			sys.exit()
		else:
			print("Пожалуста, введите нужною команду")


if __name__ == '__main__':


	while True:
		i = input("Хотите начать инру? 'y/n '").upper()
		if i == "Y":
			start()
		elif i == "N":
			sys.exit()
		else:
			print("Пожалуста, введите нужною команду")