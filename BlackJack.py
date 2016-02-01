from core import *

game = Game()

def start():
	while True:

		choices = input("Хотите карту? 'y/n' : ").upper()
		if choices == "Y":
			print(game.choice())
		elif choices == "N":
			pass

if __name__ == '__main__':

	i = input("Хотите начать инру? 'y/n '").upper()
	if i == "Y":
		start()
	elif i == "N":
		sys.exit()