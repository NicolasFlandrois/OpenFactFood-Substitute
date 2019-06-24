#!/usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

import json
from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy_utils import create_database, database_exists

from models import Product, Category

from datetime import datetime


startTime = datetime.now()
print("Setup in progress. Please wait.")

# 1/ create DB in mysql named: off1
with open("config.json") as f:
    config = json.load(f)

username = config["username"]
password = config["password"]
host = config["host"]
port = config["port"]

if not database_exists(f'mysql+pymysql://{username}:{password}@{host}/off1'):
    create_database(f'mysql+pymysql://{username}:{password}@{host}/off1')

# 2/connect to database: off1
Base = declarative_base()
engine = create_engine(
    f'mysql+pymysql://{username}:{password}@{host}/off1?host={host}?port=\
    {port}', echo=False, encoding='utf8', pool_recycle=60000,
    pool_pre_ping=True)

# 3/ Create tables in DB, named: category & product
metadata = MetaData(engine)

product = Table(
    'product', metadata,
    Column('id', Integer, primary_key=True),
    Column('ean', String(13), nullable=False),
    Column('name', String(50)),
    Column('category', Integer, ForeignKey('category.id')),
    Column('substitute', Integer, ForeignKey('product.id')),
    Column('substituted', Boolean),
    )

category = Table(
    'category', metadata,
    Column('id', Integer, primary_key=True),
    Column('label', String(50)),
    )

# 5/ creat all tables
metadata.create_all(engine)

# 4/ Fill in info to database according to tables, with seed data.

categories = ("pâte à tartiner", "confiture", "sirop")
for i in categories:
    engine.execute(category.insert(), label=i)

prods = [("3017620429484", "Nutella - Ferrero", 1, 2, False),
         ("3560070472888", "Pâte à tartiner - Carrefour Bio", 1, 1, True),
         ("5410126006957", "The original speculoos - Lotus", 1, 4, False),
         ("3700774300487", "Pâte à tartiner Speculos - Speculoos ", 1, 3,
          True),
         ("3760091721747", "Beurre de cacahuètes - Ethiquable", 1, 6, False),
         ("8710795630918", "peanut butter - Jack Klijn", 1, 5, True),
         ("3045320001525", "Confiture Extra Fraises - Bonne Maman", 2, 8,
          False),
         ("3560070986897", "Confiture de fraises - Reflets de France", 2, 7,
          True),
         ("3608580750031", "Confiture à L\'Abricot - Bonne Maman", 2, 10,
          False),
         ("3245390034830", "Confiture d\'abricots - Reflets de France", 2, 9,
          True),
         ("3045320001648", "Confiture orange - Bonne Maman", 2, 12,
          False),
         ("3245390060709", "Confiture d\'oranges - Reflets de France", 2, 11,
          True),
         ("2001111060035", "Coulis de fraises - Atelier Des Gouts Sucres", 3,
          14, False),
         ("3228170819506", "Coulis Fraises - Ponthier", 3, 13, True),
         ("3088542500278", "Pur Sirop d\'érable - Maple joe", 3, 16, False),
         ("0815126002179", "Sirop D\'érable Pur 100% - Nokomis", 3, 15, True),
         ("3088545004001", "Miel de fleurs - Lune de Miel", 3, 18, False),
         ("3088540202860", "Miel du Poitou-Charente - Miel l\'Apiculteur", 3,
          17, True)]

for index, (ean, name, category, substitute, substituted) in enumerate(prods):
    engine.execute(product.insert(), ean=ean, name=name,
                   category=category, substituted=substituted)

# create a configured "Session" class
Session = sessionmaker(bind=engine)
# create a Session
session = Session()


products = session.query(Product).all()
for n in range(0, len(products), 2):
    prod = products[n]
    sub = products[n+1]
    prod.substitute = sub.id
    sub.substitute = prod.id
session.commit()

finishTime = datetime.now()
timeDetla = finishTime-startTime

print("Setup is finished. Your database is available now.")
print("The process was completed in : " + str(
    timeDetla.total_seconds()) + "s.")

# NB ATTENTION: Improvement to provide here, for further development:
# here the databae's seed is made in a way, that the substitute follows the
# product. There for substitute is define by 1 out of 2.
# However if data seeding is organised differently,
# this script wouldn't work out. Something more automatic, more
# systematic, and accurate should be developped.
