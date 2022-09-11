
try:
	num = int(input('How old are you: '))
	print(num + 5)
except ValueError as e:
	print("You can only pass in numbers. Try again") #checks value error
except:
	print("You have made a mistake!")  #checks all errors
else:
	print("You are good to go")  #prints only when there's no error
finally:
	print("You've entered the finals")	#prints if there's no error or not 


