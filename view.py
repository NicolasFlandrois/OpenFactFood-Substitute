#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from menu import Menu
from models import Product, Category


class View(object):
	"""Views to display various infos needed through software's cicles."""
	# établire en methode statique (Statelass static avec parametre 
	#(pas de variables)) les fonction:
	
	def v_categories(self):
		"""View of all categories."""
		#Import categories from database &/or Models
		#Use repr or STR from Model, to display info in a specific display
		print(category)

	def v_products(self, category_id):
		"""View of all products within a category."""
		#Import products list form database &/or Models
		#Use repr or STR from Model, to display info in a specific display
		pass

	def product_sheet(self, product_id):
		"""View of a specific product's ID and informations. Product sheet."""
		print(product_id)
		

	def prod_sub(self, product_id):
		"""View of coresponding product and it's substitute.""" 
		product = product_id
		print("Original product: {} \n \
			Is this product corrently substituted? {} \n \
			It's substitute is {}".format(product.product_name, 
			product.substituted, product.substitute))

	def v_menu(self, question, choices):
		"""View of the menu."""
		#Import choices from v_category and v_product
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

# Translate ALL in english!

#TEST LINES
view = View
menu = Menu
product = Product
category = Category
# print(view.v_categories())
print(view.product_sheet(6, 3))
print(view.prod_sub(2, 1))