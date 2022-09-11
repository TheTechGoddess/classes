from sqlalchemy import create_engine, Column, String, ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind = engine)

class User(Base):
	__tablename__ = 'user'
	id = Column('id', Integer, primary_key = True)
	username = Column('username', String)

Base.metadata.create_all(bind = engine)
session = Session()
'''user = User(username = 'kaykay')
session.add(user)
session.commit()'''
session.close()	
users = session.query(User).filter_by(username='kaykay').first()
print(users)
print(users.username)

'''for user in users:
	print(user.username)
	print(user.id)'''

'''students = session.query(UTME).filter_by(score>=70)  picks all rows greater than 70
 or
for name in students:
	if 
	'''
	if 
