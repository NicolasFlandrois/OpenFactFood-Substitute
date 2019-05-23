#This script is kept as a reference point to create final setup.py file, using models and MVC structure in Object oriented programming
# #!usr/bin/python3.5
# # UTF8
# # Date: Wed 15 May 2019 16:58:49 CEST 
# # Author: Nicolas Flandrois

# import sqlalchemy as al
# from auth import Auth
# auth = Auth()
 
# engine = al.create_engine('mysql+pymysql://' + auth.user + ':' + auth.password + '@' + auth.host + '/off1?host=localhost?port=3306', echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)

# connection = engine.connect()
# metadata = al.MetaData()

# products =  al.Table('Products', metadata,
# 	al.Column('id', al.Integer, primary_key=True),
# 	al.Column('ean', al.String),
# 	al.Column('product_name', al.String),
# 	)
# categories = al.Table('Categories', metadata,
# 	al.Column('id', al.Integer, primary_key=True),
# 	al.Column('category', al.String),
# 	al.Column('origin_ean', al.String, al.ForeignKey('products.ean')),
# 	al.Column('substitute_ean', al.String, al.ForeignKey('products.ean')),
# 	)
# history =  al.Table('History', metadata,
# 	al.Column('id', al.Integer, primary_key=True),
# 	al.Column('origin_ean', al.String, al.ForeignKey('products.ean')),
# 	al.Column('substitute_ean', al.String, al.ForeignKey('products.ean')),
# 	al.Column('substitute_status', al.String),
# 	al.Column('date_change', al.DateTime),
# 	al.Column('comments', al.String),
# 	)
# metadata.create_all(engine)

# select = al.sql.select([products])
# results = connection.execute(select).fetchall()

# type(results)
# # for row in results:
# # 	# print(row)
# # 	for i, ident, ean, prod in enumerate(row):
# # 		print("id: ", indent, ",", "ean: ", ean, ",", "nom: ", prod)

# # class Product(Base):
# #  	"""docstring for Product"""
# #  	__tablename__ = "products"
# #  	id = Column(Integer, primary_key=True)
# #  	category = Column(Varchar)
# #  	def __init__(self, arg):
# #  		super(Product, self).__init__()
# #  		self.arg = arg
# #  		 Models(self):