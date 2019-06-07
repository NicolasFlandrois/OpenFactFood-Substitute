#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine
from models import Product, Category

engine = create_engine(
	'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
	echo=False, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()


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
		#Add possibility to: (R) Return a step back, or (Q) Quit
	

	def categories_list():
		"""View of all categories."""
		question = "Veuillez choisir une catégorie: "
		categoryList = []
		categoryQuery = session.query(Category).all()

		for choice in categoryQuery:
			categoryList.append(str(choice))
		
		return View.menu(question, categoryList)
		

	def products_list(cat_id):
		"""View of all products within a category."""
		question = "Veuillez choisir un produit : "
		productList = []
		product_ids = []
		response = session.query(Product).filter(Product.category == cat_id)

		for product in response:
			productList.append(product.name)
			product_ids.append(product.id)

		return product_ids[View.menu(question, productList)-1]


	def product_sheet(product_id):
		"""View of a specific product's ID and informations. Product sheet."""
		response = session.query(Product).filter(Product.id == product_id)
		resp_sub = session.query(Product)\
		.filter(Product.id == resp_prod.substitute)  #get à la place de filter à vérifier

		# for product in response: #Verify if this line is irelevant
		print("\
Le produit selectionné est:       {}. \n\
EAN-13:                           {}. \n\
Son substitue est                 {}. \n\
Ce produit est-il déjà substitué? {}.".format(
		response.name, response.ean, resp_sub.name, 
		response.substituted))
		return
		

	def prod_sub(product_id):
		"""View of coresponding product and it's substitute.""" 
		question = "Voulez vous substituer ce produit? "
		YesNo = ("Oui", "Non")
		prodSubList = []
		resp_prod = session.query(Product).filter(Product.id == product_id)
		resp_sub = session.query(Product).filter(Product.id == resp_prod.substitute)
		# for product in response_prod: #Verify if this line is irelevant
		print("Produit original: {} \n \
Ce produit a-t-il été déjà substitué? {} \n \
Son produit de substitution est {}".format(resp_prod.name, 
	resp_prod.substituted, resp_sub.name)) #Identify the substitute by it's name.
		
		choice = View.menu(question, YesNo)
		
		# if choice == "Oui":
		# 	#Apply substitution's changes
		# 	#Apply product.substituted = True
		# 	#Apply to sub.id.substituted = False
		# pass
		
	def History(product_id):
		"""This function will provide the poduct's substitution history."""
		#1/ al.Query How to get the history from MySQL?
		pass


#TEST LINES
# View.categories_list() #Works out
# print(View.products_list(2)) #Works out, but issue Doesn't take the choice's variable in consideration
# print(View.product_sheet(12)) #issue Doesn't take the choice's variable in consideration
# print(View.prod_sub(11)) #issue Shows the print static text, but not the data form DB & Doesn't take the choice's variable in consideration

#MAIN ISSUE: if the product.id's choice to correspond to is hardwired in the 
#codeline, it works. But if we identify the variable 'prodid', then it 
#doesn't work. PB in translation.