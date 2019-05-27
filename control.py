#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from menu import Menu
from madels import Models
from view import View


if __name__ == '__main__':
	cycle = Menu()
	#Question 0, category
	cycle.question(cycle.q[0], cycle.c0)
	#Define c1, sub-category's choices
	if cycle.c == "1":
		c1 = ("Noisette Cacao", "Speculos", "Beurre de Cacahuète")
	elif cycle.c == "2":
		c1 = ("Confiture de Fraise", "Confiture d'Abricot", "Confiture d'Orange")
	else:
		c1 = ("Coulis de Fraise", "Miel", "Sirop d'érable")
	#Question 1, Product's choices
	cycle.question(cycle.q[1], c1)
	#Question 2, Substitution Y/N
	cycle.question(cycle.q[2], cycle.c2)
	#Question 3, view Historic Y/N
	cycle.question(cycle.q[3], cycle.c2)

#Verification ALL English!