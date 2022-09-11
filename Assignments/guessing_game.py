import random

def guessing_game():
	a = int(input("Guess the number: "))
#for range of numbers 1 to 100	
	number = random.randrange(0,101)

	if  a < number:
		print("Too Low")
	elif a > number:
		print("Too High")
	else:
		print("Just Right")		

guessing_game()		
