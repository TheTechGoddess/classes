num = []
def check(x):
	if str(x) == str(x)[::-1]:
		return 1
	else:
		return 0

for i in range(100,1000):
	for j in range(100,1000):
		x=i*j
		if check(x):
			num.append(x)

print(max(num))						