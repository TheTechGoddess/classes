'''#Nested for loops
for x in range(1,11):
	for y in range(1,11):
		print(x*y, end=' ')
	print('\n')	

#while loops
i = 0
while i<=10:
	print(i)
	i+=1

while True:
	if i<=10:
		print(i)
		i+=1'''

names = ['KK', 'Lissa', 'Charles']	
i = 0
while i<len(names):
	print(names[i])	
	i+=1	

#using initial dictionary in mockup1
while i < len(students):
	if students[i]['score']<50:
		i+=1
		continue

		print(students)
		i+=1
				