from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(name,price,quantity,description,):
	p = Product(name =name ,price = price ,quantity = quantity,description = description )
	session.add(p)
	session.commit()


def update_product(id,new_quantity):
 	p = session.query(Product).filter_by(id = id ).first()
 	p.quantity = new_quantity
 	session.commit()
def delete_product(id):
		p = session.query(Product).filter_by(id = id).delete()
		session.commit()  

def get_product(id):
	p = session.query(Product).filter_by(id = id).first()
	return p

def first_product(id):
	return get_product(id)

print(first_product(1))