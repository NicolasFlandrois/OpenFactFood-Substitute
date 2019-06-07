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
		question = ("Historique de substitution? ") #Remaining question
		
	def menu(question, choices):
		"""skeleton menu's view for each query and set of question"""

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
		
	def products_list(catid):
		"""View of all products within a category."""
		question = "Veuillez choisir un produit : "
		productList = []
		productQuery = session.query(Product).filter(Product.category==catid)

		for choice in productQuery:
			productList.append(str(choice))

		return View.menu(question, productList)
		#ISSUE:
# 		File "/usr/local/lib/python3.5/dist-packages/pymysql/converters.py", line 73, in _escape_unicode
#     return value.translate(_escape_table)
# AttributeError: 'View' object has no attribute 'translate'
# & Issue this product_list() function takes only 1 argument, by giving one, it doesn't work.

	def product_sheet(prodid, *args, **kargs):
		"""View of a specific product's ID and informations. Product sheet."""
		# return session.query(Product).filter(Product.id == prod).__str__
		# return prodSheet.__str__
		prodSheet = session.query(Product).filter(Product.id == prodid)#.__str__
		prodSheet.__str__
		#Issue here, doesn't work out
		
	def prod_sub(prodid, *args, **kargs):
		"""View of coresponding product and it's substitute.""" 
		question = "Voulez vous substituer ce produit? "
		YesNo = ("Oui", "Non")
		product = session.query(Product).filter(Product.id == prodid)
		print("Produit original: {} \n \
Ce produit a-t-il été déjà substitué? {} \n \
Son produit de substitution est {}".format(Product.product_name, 
	Product.substituted, Product.substitute))
		return View.menu(question, YesNo)
		
		# if choice == "Oui":
		# 	#Apply substitution's changes
		# pass
		
#TEST LINES
view = View()
# view.categories_list() #Works out

# view.products_list() #issue Doesn't show anything
#view.product_sheet(7) #issue Doesn't show anything
view.prod_sub(8) #issue Shows the print static text, but not the data form DB