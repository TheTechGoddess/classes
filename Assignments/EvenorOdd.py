#Checking if a number is even or odd and using error handlers to test for errors from the user
def odd_even(a):
	try:
		if int(a) % 2 == 0:
			print("even")
		else:
			print("odd")
	except ValueError as e:
	    print("you have made a mistake")
	else:
		print("correct")   	
	

a = int(input("Input a number: "))

odd_even(a)	
	
