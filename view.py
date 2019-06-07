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
		productQuery = session.query(Product).filter(Product.category==10)

		for choice in productQuery:
			productList.append(str(choice))

		return View.menu(question, productList)
		#ISSUE:
# File "/usr/local/lib/python3.5/dist-packages/pymysql/converters.py", line 73, in _escape_unicode
# return value.translate(_escape_table)
# AttributeError: 'View' object has no attribute 'translate'
# & Issue this product_list() function takes only 1 argument, by giving one, it doesn't work.

	def product_sheet(choice, *args, **kargs):
		"""View of a specific product's ID and informations. Product sheet."""
		prodid = choice
		prodSheet = session.query(Product).filter(Product.id == prodid)
		for i in prodSheet:
			print(i)
		#ISSUE: if the product.id's choice to correspond to is hardwired in the 
		#codeline, it works. But if we identify the variable 'prodid', then it 
		#doesn't work. PB in translation.
		
	def prod_sub(prodid, *args, **kargs):
		"""View of coresponding product and it's substitute.""" 
		question = "Voulez vous substituer ce produit? "
		YesNo = ("Oui", "Non")
		prodSubList = []
		prodSubQuery = session.query(Product).filter(Product.id == 8)
		
		#Here find a way to separate info from the query, (not in __str__ format)		
		
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
view.products_list() #issue Doesn't take the choice's variable in consideration
# view.product_sheet() #issue Doesn't take the choice's variable in consideration
# view.prod_sub() #issue Shows the print static text, but not the data form DB