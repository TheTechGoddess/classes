#fibbonacci
x = [1,2]
i = 1
z = 0
#while the second item in the list is < 4000000
while x[i] < 4000000:
	y = x[i] + x[i-1]

	if y <= 4000000:
		x.append(y)
		i+=1
	else:
		break	
print(x)	

for i in x:
	if i % 2 == 0:
		z+=i
print(z)