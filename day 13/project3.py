#prime_numbers
def fact(x):
	factors = []
	i = 2
	while i <= x:
		while x % i == 0:
			factors.append(i)
			x/=i
		i+=1
	return factors	

print(fact(600851475142)[-1])		


