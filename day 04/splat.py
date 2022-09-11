'''*args(arguments)********************'''

'''def sum_all(*number):
	total = 0
	for i in number:
		print(f'adding {i}')
		total +=i
	print(total)	

sum_all(1,2,3,4,5,6,7,8,)'''


#when we use the splat operator, we get a tuple


'''**kwargs(keyword arguments)*******************'''

def student(**kwargs):
	print(kwargs)

name = input('what is your name: ')
age = int(input('How old are you: '))
department = input('what department are you: ')

student(name=name, age=age, department=department)	




'''def student(*args, **kwargs):
	print(args, kwargs)

name = input('what is your name: ')
age = int(input('How old are you: '))
department = input('what department are you: ')

student(1,2,3,name=name, age=age, department=department)	'''