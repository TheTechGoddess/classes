def prime(x):
	if x == 1:
		return 1
	i = 2
	while i < x:
		while x % i == 0 and x!=2:
			x/=i
			return 0
		i+=1
		
	return 1
	
for i in range(1,20):
	print(prime(i))				