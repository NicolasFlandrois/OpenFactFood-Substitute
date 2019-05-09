#!usr/bin/python3
# UTF8
# Date: Tue 07 May 2019 16:23:35 CEST 
# Author: Nicolas Flandrois
class Menu:
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