from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

from models import Product, Category

Base = declarative_base()

engine = create_engine(
	'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
	echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

#1/ create DB in mysql named: off1

#2/ Create tables in DB, named: category & product

#3/ Fill in info to db according to tbls

#4/ creat all
Base.metadata.create_all(engine)