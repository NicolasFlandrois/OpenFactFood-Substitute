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

# product = Product
# category = Category

class View(object):
	"""Views to display various infos needed through software's cicles."""
	
	choice = 0
	question = ("Veuillez choisir une catégorie: ",
	"veuillez choisir un produit : ",
	"Voulez vous substituer ce produit? ", 
	"Historique de substitution? ")
	#Sustitution & Historic's choices Yes/No
	YesNo = ("Oui", "Non")

	@staticmethod	
	def categories_list():
		"""View of all categories."""
		category_list = session.query(Category).all()
		menu(question[0], categories_list)
		#use menu to display

	@staticmethod
	def products_list(choice):
		"""View of all products within a category."""
		product_list = session.query(Product).filter(
			product.category == choice)
		print(product_list)
	
	@staticmethod
	def product_sheet(choice):
		"""View of a specific product's ID and informations. Product sheet."""
		prod_sheet = session.query(Product).filter(
			product.id == choice).__str__
		print(prod_sheet)
		
	@staticmethod
	def prod_sub(choice):
		"""View of coresponding product and it's substitute.""" 
		# product = session.query(Product).filter(
		# 	Product.id == choice)
		product = session.query(Product).all().filter(
			Product.id == choice)
		print("Original product: {} \n \
			Is this product corrently substituted? {} \n \
			It's substitute is {}".format(product.product_name, 
			product.substituted, product.substitute))
		
	@staticmethod
	def menu(question, choices):

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
# view.categories_list() #issue Doesn't show anything
# view.products_list(2) #issue Doesn't show anything
# view.product_sheet(7) #issue Doesn't show anything
view.prod_sub(8) #issue Shows the print static text, but not the data form DB