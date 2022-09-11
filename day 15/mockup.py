#for loops
numbers = [i for i in range(1,100)]
#print(numbers)

#the above is the same as :-
num = []
for i in range(1,101):
	num.append(i)
print(num)

student = ["KK", "Lissa", "Chioma"]	
	
for i in range(len(student)):
	#print(student[i])
	if i == 150:
		break

#looping through a dictionary
students = [{"name":"KK", "score":"70"},{"name":"Lissa", "score":"85"}]		
for student in students:
	#print(student["name"], end=' ')
	#print(student["score"])

#students that scored above 50
for i in students:
	if i["score"]>=50:
		#print(i["name"])	

#150 students that score above 150
k = 1 
for i in students:
	if k>=150:	
		break
	if i["score"]>=50:
		print(i["name"])
		k+=1


