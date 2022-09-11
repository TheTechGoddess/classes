def firstlast(x):
	y = type(x)(x[0]+x[-1])
	print(y)	
	return y

firstlast('abc')	