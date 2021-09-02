age = int(input("How old are you: "))
department = input("What is your department: ")

'''if age < 18:
	print('You are too young!')
elif age>=18 and age<=30:
	print('You are a youth!')
elif age>=31 and age<=95:
    print('You should marry!')
else:
    print('God pass you')    	

'''

if age > 18:
	print('You are a youth!')
	if department == 'ECE':
		print('You are welcome!')
	else:
	    print('We do not recognize this department!')
else:
    print('You are too young!')	

        	