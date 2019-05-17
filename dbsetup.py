#!usr/bin/python3.5
# UTF8
# Date: Wed 15 May 2019 16:58:49 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from auth import Auth
auth = Auth()
 
engine = al.create_engine('mysql+pymysql://' + auth.user + ':' + auth.password + '@' + auth.host + '/off1?host=localhost?port=3306', echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

connection = engine.connect()

#test
# base = connection.execute("SHOW Tables").fetchall()
# print(base)
#Attempt to read a specific table, then enumerate and append a list/tuple in python
# select = al.select('category').select_from('Categories')
# results = connection.execute(select).fetchall()

for row in connection.execute(al.select([Categories, products])):
	print(row)


# class Product(Base):
#  	"""docstring for Product"""
#  	__tablename__ = "products"
#  	id = Column(Integer, primary_key=True)
#  	category = Column(Varchar)
#  	def __init__(self, arg):
#  		super(Product, self).__init__()
#  		self.arg = arg
#  		 Models(self):