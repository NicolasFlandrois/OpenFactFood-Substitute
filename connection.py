#!/usr/bin/python3.7
# UTF8
# Date: 
# Author: Nicolas Flandrois

import json
from urllib.request import urlopen

import sqlalchemy as al
from sqlalchemy.orm import sessionmaker, query
from sqlalchemy import create_engine, update

def connect():

	with open("config.json") as f:

		config = json.load(f)

		username = config["username"]
		password = config["password"]
		host = config["host"]
		port = config["port"]

		engine = create_engine(
			f'mysql+pymysql://{username}:{password}@{host}/off1?host={host}?port=\
			{port}', echo=False, encoding='utf8', pool_recycle=60000,
			pool_pre_ping=True)

		Session = sessionmaker(bind=engine)
		session = Session()

		return session
