n = 1000
pyth = [1,2]

for i in range(pyth[1], n):
	for j in range(pyth[0], pyth[1]):
		c = n - i - j
		if i**2 + j**2 == c**2:
			print(i*j*c)
			break
	pyth[1] += 1		