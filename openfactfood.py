#!usr/bin/python3
# UTF8
# Date: Tue 07 May 2019 16:23:35 CEST 
# Author: Nicolas Flandrois
class Question:
	"""This class defines the menu and questions 
	to navigate through the script."""
	
	def __init__(self, question, *choices):
		self.question = ""
		self.choices =  []
		self.c = None


	def menu(self, question, choices):
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
		choicetxt = choices[choice-1]
		print("Vous avez choisit: " + choicetxt)
		self.c = str(choice)

#Category menu's questions & choices
c = None
q0 = "Veuillez choisir une catégorie: "
c0 = ['pâte à tartiner', 'confiture', 'coulis']
#Products's questions & choices
q1 = "veuillez choisir un produit : "
c1 = []
#Sustitution's questions & choices
q2 = "Voulez vous substituer ce produit? "
c2 = ["Oui", "Non"]
#Substitutes Historic's questions & choices
q3 = "Historique de substitution? "
c3 = ["Oui", "Non"]

#TESTS LINES
quest0 = Question(q0, c0)
quest0.menu(q0, c0)

if quest0.c == "1":
	c1 = ["Noisette Cacao", "Speculos", "Beurre de Cacaouette"]
elif quest0.c == "2":
	c1 = ["Confiture de Fraise", "Confiture d'Abricot", "Confiture d'Orange"]
else:
	c1 = ["Coulis de Fraise", "Miel", "Sirop d'érable"]
quest1 = Question(q1, c1)
quest1.menu(q1, c1)

quest2 = Question(q2, c2)
quest2.menu(q2, c2)

quest3 = Question(q3, c3)
quest3.menu(q3, c3)