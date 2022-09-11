x = 2000000
sum_ = 0
primes_list = [True for i in range(x+1)]

p = 2

while (p*p <= x):
	if primes_list[p]:
		for i in range(p*p, x+1, p):
			primes_list[i] = False
	p+=1
	
for i in range(2, x+1):
	if primes_list[i]:
		sum_+=i

print(sum_)					