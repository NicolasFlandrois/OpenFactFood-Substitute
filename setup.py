#!usr/bin/python3.5
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST 
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, String, Boolean 
from sqlalchemy import create_engine, MetaData, ForeignKey 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
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

Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

#3/ Create tables in DB, named: category & product

#4/ Fill in info to db according to tbls

#5/ creat all
#Base.metadata.create_all(engine)