#!/usr/bin/python3.7
# UTF8
# Date: Thu 09 May 2019 14:40:35 CEST
# Author: Nicolas Flandrois

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connection import connect

session = connect()

Base = declarative_base()


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
    name = Column(String(50))

    def __repr__(self):
        return str((self.name))
