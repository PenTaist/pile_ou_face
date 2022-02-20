import random
import os

os.system("cls")

running = True


def start():
	os.system("color a")
	print("Pile = heads     Face = tails")
	print(" ")
	demande = input("Tapez 'go' / type 'go' : ")

	if demande == "go":
		game()
	else:
		print("Veuillez écrire go et pas autre chose ! / Please write go and nothing else !")


def running():
	if running == True:
		game()
	else:
		os.system("exit")


def restart():
	restart = input("Voulez vous rejouer ? (oui ou non) / Do you want to play again? (yes or no) : ")

	if restart == "oui":
		game()
	elif restart == "yes":
		game()
	else: 
		running = False
		os.system("color 7")
		os.system("cls")
		print("Merci d'avoir joué ! / Thanks for playing !")


def game():
	gen = random.randrange(3)
	if gen == 1:
		print(" ")
		print("Pile !")
		print(" ")
		restart()
	elif gen == 2:
		print(" ")
		print("Face !")
		print(" ")
		restart()
	else:
		game()


start()
