#prime_numbers
def fact(x):
	factors = []
	prime = []
	for i in range(2,x):
		
		if x % i == 0:
			factors.append(i)
		print(factors)
	return factors

def prime(x):
	prime_numbers = []
	for i in x:
		if len(prime_numbers) < 1 :
			y = fact(i)
			if y == []:
				prime_numbers.append(i)
		else:
			break
	return prime_numbers		

a = fact(600851475143)
b = prime(a[::-1])
print(b)

#do not run... this will hang your system. check out project3.py for better algorithm
