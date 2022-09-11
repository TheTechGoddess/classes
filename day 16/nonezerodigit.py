N = 4 
A = [3,23,30,45]
product = 1

for i in A:
	product*=i

product=str(product)
product_split = ','.join(product).split(',')	
for i in range(len(product_split)):
	if int(product_split[-(i+1)]) != 0:
		print(product_split[-(i+1)])
		break
