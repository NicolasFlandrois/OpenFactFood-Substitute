#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from menu import Menu
from models import Product, Category
menu = Menu
product = Product
category = Category

class View(object):
	"""docstring for View"""
	# def __init__(self, arg):
	# 	super(View, self).__init__()
	# 	self.arg = arg

	def v_category(self):
		"""View of all categories."""
		#Import categories from 
		pass

	def v_product(self):
		"""View of all products within a category."""
		pass

	def product_card(self):
		"""View of a specific product's ID and informations. Product sheet."""
		pass

	def prod_sub(self):
		"""View of coresponding product and it's substitute."""
		pass

	def v_menu(self, question, choices):
		"""View of the menu."""
		#Import choices from v_category
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

# class View
# établire en methode statique (Statelass static avec parametre (pas de variables)) les fonction:
# • category (e.g. view.category(category) > self.category(param))
# • view produit par catégories
# • view 1 produit spécifique
#    ◇ Fiche produit
# • view 1 produit et son substitut
# • view menu
#    ◇ reprendre ce qui a été fait dans fichier menu
#    ◇ faire 1 view par menu
#    ◇ vue bloquante > attends une réponce
#       ▪ affichage
#       ▪ input
#       ▪ output
#    ◇ stateless
#       ▪ static
#       ▪ param
#       ▪ (pas de variables en param)
# Translate ALL in english!