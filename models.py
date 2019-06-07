#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(
	'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
	echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)


Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

class Product(Base):
	"""docstring for Products"""
	__tablename__ = "product"
	id = Column(Integer, primary_key=True)
	ean = Column(String(13), nullable=False)
	product_name = Column(String(50))
	category = Column(Integer, ForeignKey('category.id'))
	substitute = Column(Integer, ForeignKey('product.id'))
	substituted = Column(Boolean)

	def __str__(self):
		return "\
Le produit selectionné est:       {}. \n\
EAN-13:                           {}. \n\
Son substitue est                 {}. \n\
Ce produit est-il déjà substitué? {}.".format(
			self.product_name, self.ean, self.substitute, self.substituted)
	
class Category(Base):
	"""docstring for Categories"""
	__tablename__ = "category"
	id = Column(Integer, primary_key=True)
	label = Column(String(50))
	
	def __repr__(self):
		return str((self.label))
