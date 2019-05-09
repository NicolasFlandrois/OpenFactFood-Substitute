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
q2 = "Question 2 : "
c2 = ["A", "B", "C"]
#xyz3's questions & choices
q3 = "Question 3"
c3 = ["K", "L", "M"]
#xyz4's questions & choices
q4 = "Question 4"
c4 = ["X", "Y", "Z"]

#TESTS LINES
quest1 = Question(q1, c1)
quest1.menu(q1, c1)
quest2 = Question(q2, c2)
quest2.menu(q2, c2)
quest3 = Question(q3, c3)
quest3.menu(q3, c3)
quest4 = Question(q4, c4)
quest4.menu(q4, c4)