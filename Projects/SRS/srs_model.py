from sqlalchemy import create_engine, Column, String, ForeignKey,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///srs.db')
Session = sessionmaker(bind = engine)

class Student(Base):
	__tablename__ = 'students'
	id = Column('id', Integer, primary_key = True)
	name = Column('name', String)
	gender = Column('gender', String)
	grade = Column('grade', String)
	dob = Column('dob', String)
	sor = Column('state_of_origin', String)
	

Base.metadata.create_all(bind = engine)
session = Session()
'''students = Student(name = 'kaykay', gender = 'M', grade = 'Jss1', dob = '16th November 1997', sor = 'Anambra')
session.add(students)
session.commit()'''
'''student = session.query(Student).all()
student[0].gender = 'M'
student[0].grade = 'Jss1'
student[0].dob = '16th November, 1997'
student[0].sor = 'Anambra'''
#session.commit()
#students = Student(name = 'Cheta', gender = 'F', grade = 'Jss2', dob = '23rd November 1993', sor = 'Enugu')
'''student[1].gender = 'F'
student[1].grade = 'Jss2'
student[1].dob = '23th November, 1993'
student[1].sor = 'Enugu'''
#session.add(students)
#session.commit()
print(student[1].name)
