import random
import os

os.system("cls")

running = True


def start():
	os.system("color a")
	demande = input("Tapez 'prêt' : ")

	if demande == "prêt":
		game()
	else:
		print("Veuillez écrire prêt et pas autre chose !")


def running():
	if running == True:
		game()
	else:
		os.system("exit")


def restart():
	restart = input("Voulez vous rejouer ? (oui ou non) : ")

	if restart == "oui":
		game()
	else: 
		running = False
		os.system("color 7")
		print("Merci d'avoir joué !")


def game():
	gen = random.randrange(3)
	if gen == 1:
		print("Pile !")
		restart()
	elif gen == 2:
		print("Face !")
		restart()
	else:
		game()


start()
