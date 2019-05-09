#!usr/bin/python3
# UTF8
# Date: Tue 07 May 2019 16:23:35 CEST 
# Author: Nicolas Flandrois
class Question:
	"""This class defines the menu and questions 
	to navigate through the script."""
	
	def __init__(self, question, choices**):#Why the "choices**"
		self.question = ""#"veuillez choisir une catégorie: "
		self.choices =  []#['pâte à tartiner', 'confiture', 'coulis']


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
		return choice

#Category menu's questions & choices
q1 = "veuillez choisir une catégorie: "
c1 = ['pâte à tartiner', 'confiture', 'coulis']
#xyz2's questions & choices
q2 = ""
c2 = []
#xyz3's questions & choices
q3 = ""
c3 = []
#xyz4's questions & choices
q4 = ""
c4 = []

#TESTS LINES
quest = Question(q, c)
quest.menu(q, c)