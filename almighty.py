import math


def almighty(a,b,c):
	top = abs(b**2 - (4*a*c))
	d = (-b + math.sqrt(top))/2*a
	e = (-b - math.sqrt(top))/2*a
	x = (d,e)
	return x

print(almighty(1,2,3))