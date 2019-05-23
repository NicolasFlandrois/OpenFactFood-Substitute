from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine(
	'mysql+pymysql://odin:lincoln@localhost/off1?host=localhost?port=3306', 
	echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)



Base.metadata.create_all(engine)