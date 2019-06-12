#!usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

import json
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("config.json") as f:
    config = json.load(f)

username = config["username"]
password = config["password"]
host = config["host"]
port = config["port"]

Base = declarative_base()

engine = create_engine(
    f'mysql+pymysql://{username}:{password}@{host}/off1?host={host}?port=\
    {port}', echo=False, encoding='utf8', pool_recycle=60000,
    pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()


class Product(Base):
    """docstring for Products"""
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    ean = Column(String(13), nullable=False)
    name = Column(String(50))
    category = Column(Integer, ForeignKey('category.id'))
    substitute = Column(Integer, ForeignKey('product.id'))
    substituted = Column(Boolean)


class Category(Base):
    """docstring for Categories"""
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    label = Column(String(50))

    def __repr__(self):
        return str((self.label))
