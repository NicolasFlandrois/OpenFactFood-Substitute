#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine
from menu import Menu
from models import Product, Category

engine = create_engine(
	'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
	echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

product = Product
category = Category

class View(object):
	"""Views to display various infos needed through software's cicles."""
	# établire en methode statique (Stateless static avec parametre 
	#(pas de variables)) les fonction:
	
	@staticmethod	
	def categories_list():
		"""View of all categories."""
		#Import categories from database &/or Models
		#Use repr or STR from Model, to display info in a specific display
		categories_list = session.query(category)
		print(category)

	@staticmethod
	def products_list(choice):
		"""View of all products within a category."""
		#Import products list form database &/or Models
		#Use repr or STR from Model, to display info in a specific display
		products_list = session.query(product).filter(
			product.category == choice)
		print(products_list)

	@staticmethod
	def product_sheet(choice):
		"""View of a specific product's ID and informations. Product sheet."""
		
	@staticmethod
	def prod_sub(choice):
		"""View of coresponding product and it's substitute.""" 
		#xxxdefine choice
		print("Original product: {} \n \
			Is this product corrently substituted? {} \n \
			It's substitute is {}".format(product.product_name, 
			product.substituted, product.substitute))

	@staticmethod
	def v_menu(question, choices):
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
		return choice

# Translate ALL in english!

#TEST LINES
view = View()
print(view.categories_list())
