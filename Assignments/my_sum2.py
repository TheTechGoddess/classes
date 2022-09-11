def my_sum(*x):
	y = ''
	z = []
	v = 0

	for i in x:
		if i == str(i):
			y+=i

		elif i == list(i):
			z+=i

		elif i == int(i):
			v+=i
		else:
			pass
	print(y)
	print(z)
	print(v)


my_sum([1,2,3],[4,5,6])
my_sum('abc','def')					
my_sum(1,2,3)
