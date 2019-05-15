#!usr/bin/python3
# UTF8
# Date:  Wed 15 May 2019 16:58:49 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al

engine = al.create_engine('mysql://xxxxxx', echo=True)
#Add DB path here

class Product(Base):
 	"""docstring for Product"""
 	__tablename__ = "products"
 	id = Column(Integer, primary_key=True)
 	category = Column(Varchar)
 	def __init__(self, arg):
 		super(Product, self).__init__()
 		self.arg = arg
 		 Models(self):