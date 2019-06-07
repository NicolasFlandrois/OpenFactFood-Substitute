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
	
	def __init__(self):
		self.choice = 0
		question = (
		"",
		"Voulez vous substituer ce produit? ", 
		"Historique de substitution? ")
		#Sustitution & Historic's choices Yes/No
		YesNo = ("Oui", "Non")

	def menu(question, choices):

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
	
	def categories_list(*args, **kargs):
		"""View of all categories."""
		question = "Veuillez choisir une catégorie: "
		categoryList = []
		categoryQuery = session.query(Category).all()

		for choice in categoryQuery:
			categoryList.append(str(choice))
		
		return View.menu(question, categoryList)
		
	def products_list(cat):
		"""View of all products within a category."""
		question = "Veuillez choisir un produit : "
		productList = []
		productQuery = session.query(Product).filter(Product.category==cat)

		for choice in productQuery:
			productList.append(str(choice))

		return View.menu(question, productList)
		#ISSUE:
# 		File "/usr/local/lib/python3.5/dist-packages/pymysql/converters.py", line 73, in _escape_unicode
#     return value.translate(_escape_table)
# AttributeError: 'View' object has no attribute 'translate'

	def product_sheet(choice):
		"""View of a specific product's ID and informations. Product sheet."""
		prod_sheet = session.query(Product).filter(
			product.id == choice).__str__
		print(prod_sheet)
		
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
		
#TEST LINES
view = View()
# view.categories_list() #Works out

view.products_list() #issue Doesn't show anything
# view.product_sheet(7) #issue Doesn't show anything
# view.prod_sub(8) #issue Shows the print static text, but not the data form DB