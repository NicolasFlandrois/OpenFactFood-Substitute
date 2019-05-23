#!usr/bin/python3.5
# UTF8
# Date: Tue 07 May 2019 16:23:35 CEST 
# Author: Nicolas Flandrois

class Menu:
	"""This class defines the menu and questions 
	to navigate through the script."""
	
	#def __init__(self, question, *choices):
	def __init__(self):	
		self.c = 0
		self.q = ("Veuillez choisir une catégorie: ",
		"veuillez choisir un produit : ",
		"Voulez vous substituer ce produit? ", 
		"Historique de substitution? ")
		#Category menu's choices
		self.c0 = ("pâte à tartiner", "confiture", "liquide")
		#Products's choices
		#c1's list will be define later depending on previous answer
		#Sustitution & Historic's choices Yes/No
		self.c2 = ("Oui", "Non")


	def question(self, question, choices):
		choice = None

		print(question)

		for num, choice in enumerate(choices):
			print(str(num+1) + " : "+ choice)

		while True:
			try:
				choice = int(input())
				if choice in range(1, len(choices)+1):
					break
				else:
					raise
			except:
				print(
					"Veuillez entrer un nombre entre 1 et " 
					+ str(len(choices)) + "."
					)
		print("Vous avez choisi: " + choices[choice-1])
		self.c = choice