#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, String, Boolean, Table 
from sqlalchemy import create_engine, MetaData, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy_utils import create_database, database_exists 

from models import Product, Category

#1/ create DB in mysql named: off1
if not database_exists("mysql+pymysql://odin:lincoln@localhost/off1"):
	create_database("mysql+pymysql://odin:lincoln@localhost/off1")

#2/connect to database: off1
#Base = declarative_base() #Not usefull here
engine = create_engine(
	'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
	echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

Session = sessionmaker(bind=engine) #not in use yet
session = Session() #not in use yet
metadata = MetaData()

#3/ Create tables in DB, named: category & product
product = Table(
	'product', metadata,
	Column('id', Integer, primary_key=True),
	Column('ean', String(13), nullable=False),
	Column('product_name', String(50)),
	Column('category', Integer, ForeignKey('category.id')),
	Column('substitute', Integer, ForeignKey('product.id')),
	Column('substituted', Boolean),
	)

category = Table(
	'category', metadata,
	Column('id', Integer, primary_key=True),
	Column('label', String(50)),
	)

#5/ creat all tables
metadata.create_all(engine)

#4/ Fill in info to db according to tbls
