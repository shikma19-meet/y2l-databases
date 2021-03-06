from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
	__tablename__ = 'products'
	id = Column(Integer,primary_key = True)
	name = Column(String)
	price = Column(Float)
	quantity = Column(Float)
	description = Column(String)
   
