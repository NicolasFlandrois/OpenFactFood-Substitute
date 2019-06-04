#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, String, Boolean, Table 
from sqlalchemy import create_engine, MetaData, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy_utils import create_database, database_exists 

from models import Product, Category

#1/ create DB in mysql named: off1
if not database_exists("mysql+pymysql://odin:lincoln@localhost/off1"):
    create_database("mysql+pymysql://odin:lincoln@localhost/off1")

#2/connect to database: off1
Base = declarative_base()
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

# #5/ creat all tables
# metadata.create_all(engine)

# #4/ Fill in info to database according to tables, with seed data.

# categories = ("pâte à tartiner", "confiture", "sirop")
# for i in categories:
#     engine.execute(category.insert(), label=i)

# prods = [("3017620429484", "Nutella - Ferrero - 825 g", 1, 2, False),
#     ("3560070472888", "Pâte à tartiner - Carrefour Bio - 350 g", 1, 1, True),
#     ("5410126006957", "The original speculoos - Lotus - 400 g", 1, 4, False),
#     ("3700774300487", "Pâte à tartiner Speculos - Speculoos ", 1, 3, True),
#     ("3760091721747", "Beurre de cacahuètes - Ethiquable - 350 g", 1, 6, False),
#     ("8710795630918", "peanut butter - Jack Klijn - 350 gr", 1, 5, True),
#     ("3045320001525", "Confiture Extra Fraises - Bonne Maman - 370 g", 2, 8, \
#         False),
#     ("3245390163868", "Confiture extra de fraises du Perigord - \
# Reflets de France", 2, 7, True),
#     ("3608580750031", "Confiture à L\'Abricot Fruitée Intense - Bonne Maman - \
# 340 g", 2, 10, False),
#     ("3245390034830", "Confiture d\'abricots du Roussillon - Reflets de France \
# - 325 g", 2, 9, True),
#     ("3045320001648", "Confiture orange en tranches - Bonne Maman - 370 g", 2, \
#         12, False),
#     ("3245390060709", "Confiture d\'oranges et de clémentines de Corse - \
# Reflets de France - 325 g", 2, 11, True),
#     ("2001111060035", "Coulis de fraises cuit à la marmite - Atelier Des Gouts \
# Sucres", 3, 14, False),
#     ("3228170819506", "Coulis Fraises Ponthier - 1 Kg", 3, 13, True),
#     ("3088542500278", "Pur Sirop d\'érable - Maple joe - 250 g", 3, 16, False),
#     ("0815126002179", "Sirop D\'érable 250g Pur 100% Origine Canada - Nokomis \
# - 250 g", 3, 15, True),
#     ("3088545004001", "Miel de fleurs - Lune de Miel - 500 g", 3, 18, False),
#     ("3088540202860", "Miel l\'Apiculteur : Poitou-Charente"," Le Pot 500G \
# - 500 g", 3, 17, True)]

# for index, (ean, name, category, substitute, substituted) in enumerate(prods):
#         engine.execute(product.insert(), ean=ean, product_name=name, 
#             category=category, substituted=substituted)
#Investigation ISSUE: this engine.execute(product.insert) for loop doesn't insert this product 
#succesfully 3088540202860, last item on the list. WHY? HOW?
# And return following error:
# 2019-06-04 16:56:25,386 INFO sqlalchemy.engine.base.Engine COMMIT
# Traceback (most recent call last):
#   File "/media/odin/RAGNAROCK_BACKUP/OFFood/setup.py", line 80, in <module>
#     for index, (ean, name, category, substitute, substituted) in enumerate(prods):
# ValueError: too many values to unpack (expected 5)
#https://stackoverflow.com/questions/48390207/sql-alchemy-valueerror-too-many-values-to-unpack
#The script cannot persue the next commands then. So it's not an issue it cannot update, but an issue it cannot continue.

# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()


products = session.query(Product).all()
print(products) #Test, ok this works out
for n in range(0, len(products), 2):
    prod = products[n]
    sub = products[n+1]
    prod.substitute = sub.id
    sub.substitute = prod.id
    session.commit()
#NB: ISSUE with this last command, the DB don't commit the update.
#Traceback (most recent call last):
#   File "/media/odin/RAGNAROCK_BACKUP/OFFood/setup.py", line 104, in <module>
#     prod.substitute = sub.id
# AttributeError: can't set attribute
    
#NB ATTENTION: Improvement to provide here, for further development: 
#here the databae's seed is made in a way, that the substitute follows the 
#product. There for substitute is define by 1 out of 2. 
#However if data seeding is organised differently, 
#this script wouldn't work out. Something more automatic, more 
#systematic, and accurate should be developped.
