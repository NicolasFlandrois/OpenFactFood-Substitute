#!usr/bin/python3
# UTF8
# Date: Wed 15 May 2019 16:58:49 CEST 
# Author: Nicolas Flandrois

import sqlalchemy as al
from auth import Auth
auth = Auth()

engine = al.create_engine('mysql://'+auth.user+'@'+auth.host+'/off1:'+auth.port,
echo=True) #need to select the database within mysql/mariadb and if not exist, create it during setup. 
connection = engine.connect()

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

class Product(Base):
 	"""docstring for Product"""
 	__tablename__ = "products"
 	id = Column(Integer, primary_key=True)
 	category = Column(Varchar)
 	def __init__(self, arg):
 		super(Product, self).__init__()
 		self.arg = arg
 		 Models(self):