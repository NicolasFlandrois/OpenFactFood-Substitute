#!usr/bin/python3.5
# UTF8
# Date: Wed 15 May 2019 16:58:49 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from auth import Auth
auth = Auth()
 
engine = al.create_engine('mysql+pymysql://' + auth.user + ':' + auth.password + '@' + auth.host + '/off1?host=localhost?port=3306', echo=True, encoding='utf8', pool_recycle=60000, pool_pre_ping=True)
#need to select the database within mysql/mariadb and if not exist, 
#create it during setup. 
connection = engine.connect()
connection.execute("SELECT host FROM INFORMATION_SCHEMA.PROCESSLIST WHERE ID = CONNECTION_ID()").fetchall()

# base = sqlalchemy.ext.declarative.declarative_base()
# metadata = base.metadata.create_all(engine)
# print(metadata)

# def get_session(debug=False):
#     engine = create_engine('mysql://root:pw@IP/DB', echo=debug, encoding='utf8', pool_recycle=300, pool_pre_ping=True)
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     try:
#         yield session
#         session.commit()
#     except:
#         session.rollback()
#         raise
#     finally:
#         session.close()

# class Product(Base):
#  	"""docstring for Product"""
#  	__tablename__ = "products"
#  	id = Column(Integer, primary_key=True)
#  	category = Column(Varchar)
#  	def __init__(self, arg):
#  		super(Product, self).__init__()
#  		self.arg = arg
#  		 Models(self):