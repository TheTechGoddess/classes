def calc(b, c):
	a = b+c
	return a

print(calc(3, 4))	

def intro(name, age, department):
	print(f'Your name is {name}, you are {age} years old  and you are in {department}.')

'''Positional Argument
intro('Lissa', 21, 'EE')'''


'''Keyword Argument
intro(name='Lissa', age=21, department='EE')'''


'''Default Argument
def intro(name='Cheta', age=26, department='ECE'):
	print(f'Your name is {name}, you are {age} years old  and you are in {department}.')

intro(name='Lissa', age=21, department='EE')'''