'''x = 0

fruits = ["apple", "banana", "watermelon", "cherry", "orange"]



while x < len(fruits):
	print(f'{x+1}. {fruits[x]}')
	x+=1'''

students = [{"name":"Ikem", "department": "ECE", "score":60}, {"name":"Presh", "department": "ECE", "score":75 },{"name":"Cheta", "department": "ECE", "score":40},{"name":"Emma", "department": "ELE", "score":25}]

x = 0

'''print("S/N\t Name\t Department")

while x < len(students):
	print(f' {x+1}.\t {students[x]["name"]}\t {students[x]["department"]}\t {students[x]["score"]}')
	x+=1'''



'''while x < len(students):
	print(f'{students[x]["name"]} => {students[x]["department"]}')
	x+=1'''
passed = []
failed = []

while x < len(students):
	if students[x]["score"] > 50:
		print(passed.append(students[x]))
	else:
		print(failed.append(students[x]))
	x+=1
			