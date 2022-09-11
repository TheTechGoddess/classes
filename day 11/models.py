from sqlalchemy import create_engine, Column, String, ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind = engine)

class User(Base):
	__tablename__ = 'user'
	id = Column('id', Integer, primary_key = True)
	fullname = Column('Fullname', String)
	account_id = Column('Account_id', String, unique = True)
	balance = Column('Balance', Integer)

Base.metadata.create_all(bind = engine)	
