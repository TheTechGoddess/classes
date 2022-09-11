names = ['KK'......1000]
x= 0
while x<len(names):
	print(names[x])
 	x+=1
 	if x == 150:
 		break

#to print names of students with scores greater than 50 from dictionary
while x<len(names):
	if x['scores']<50:
		x+=1
		continue

	print(names[x])
	x+=1

for x in names:
	if x['scores']<50:
		continue
	print(x)				