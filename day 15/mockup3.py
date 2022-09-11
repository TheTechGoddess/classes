#Functions (calculator)
def sum(x,y):
	z = x+y
	return z

print(sum(3,5))

#using splat operator
def market (*items):
	print(items)

k = market('milo','market','board')
print(k)

#*args prints multiple arguments6
start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
i = 0

#**kwargs prints dictionary
def student(**kwargs):
	print(kwargs)

student('name':'KK')

#recussion is callinga function in itself. 
def fib(x,y):
	return fib(y,x+y)
