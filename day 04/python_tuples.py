fruits = ('apple', 'banana', 'pear')

empty_fruits =()

one_fruit = ('yam',)

#accessing items from tuple is the same as accessing from lists. They can as well hold different data types including lists
#you can't modify a tuple unless you change it to a list

list_fruits = list(fruits)

list_fruits[0] = 'lemon'

fruits = tuple(list_fruits)

print(fruits)