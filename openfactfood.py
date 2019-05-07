#!usr/bin/python3
# UTF8
# Date: Tue 07 May 2019 16:23:35 CEST 
# Author: Nicolas Flandrois
class Question:
	"""This class defines the menu and questions 
	to navigate through the script."""
	
	def __init__(self, question, choices**):
		#Stocker selfquestion & self choices
		self.question = "veuillez choisir une catégorie: "
		self.choices = ['pâte à tartiner', 'confiture', 'salé']


def menu(choices, question):
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
	return choice
