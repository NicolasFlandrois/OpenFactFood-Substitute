#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from sqlalchemy import Column, Integer, String, Boolean, Table 
from sqlalchemy import create_engine, MetaData, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy_utils import create_database, database_exists 
import csv
# from numpy import genfromtxt 

from models import Product, Category

#1/ create DB in mysql named: off1
if not database_exists("mysql+pymysql://odin:lincoln@localhost/off1"):
    create_database("mysql+pymysql://odin:lincoln@localhost/off1")

#2/connect to database: off1
#Base = declarative_base() #Not usefull here
engine = create_engine(
    'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
    echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

#3/ Create tables in DB, named: category & product
metadata = MetaData(engine)

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

categories = ("pâte à tartiner", "confiture", "sirop")
for i in categories:
    engine.execute(category.insert(), label=i)

#Products' data import isn't working this way, should make it more simple
#Extracting data from csv with python, feeding a list of tuples
#The enumerate() or for loop to feed the Table's DB

# with open('products.csv') as csvfile:
#     prod = [n for n in csvfile.read().replace(",", "").replace("\n", "")]

# print(prod)

engine.execute("""
    LOAD DATA LOCAL INFILE 'products.csv'
    INTO TABLE product
    FIELDS TERMINATED BY ',' ENCLOSED BY '"'
    LINES TERMINATED BY '\\n'
    (ean, product_name, category, substitute, substituted);
    """)

# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter=',',  
#         converters={0: lambda s: str(s)})
#     return data.tolist()

# session = sessionmaker()
# session.configure(bind=engine)
# s = session()

# try:
#     file_name = "products.csv"
#     data = Load_Data(file_name) 

#     for i in data:
#         record = product(**{
#             'ean' : i[0],
#             'product_name' : i[1],
#             'category' : i[2],
#             'substitute' : i[3],
#             'substituted' : i[4]
#         })
#         s.add(record) #Add all the records

#     s.commit() #Attempt to commit all the records
# except:
#     s.rollback() #Rollback the changes on error
# finally:
#     s.close() #Close the connection