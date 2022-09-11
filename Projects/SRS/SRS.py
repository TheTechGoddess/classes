no_of_students = int(input('No of Students: '))
name = input('name of student: ')
gender = input('gender: ')
grade = input('grade: ')
dob = input('dob: ')
state_of_origin = input('state_of_origin: ')


class Students(): 
	students = []
	def __init__(self,name,gender,grade,dob,state_of_origin):
		self.name = name
		self.gender = gender
		self.grade = grade
		self.dob = dob
		self.state_of_origin = state_of_origin

student1 = Students(name = name, gender = gender, grade = grade, dob = dob, state_of_origin = state_of_origin)
print(student1.name)



