
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
from auth import Auth
auth = Auth()

engine = create_engine('mysql+pymysql://' + auth.user + ':' + auth.password + '@' + auth.host + '/off1?host=localhost?port=3306', echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

class Product(Base):
	"""docstring for Products"""
	__tablename__ = "product"
	id = Column(Integer, primary_key=True)
	ean = Column(String(13))
	product_name = Column(String(50))
	category = Column(Integer, ForeignKey('category.id'))
	substitute = Column(Integer, ForeignKey('product.id'))
	substituted = Column(Boolean)
	
class Category(Base):
	"""docstring for Categories"""
	__tablename__ = "category"
	id = Column(Integer, primary_key=True)
	label = Column(String(50))

Base.metadata.create_all(engine) #à mettre dans un autre fichier! après avoir charger les models

pateatartiner = Category(label="pâte à tartiner")
session.add(pateatartiner)
confiture = Category(label="confiture")
sirop = Category(label="sirop")