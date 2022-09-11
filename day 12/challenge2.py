x=1; y=2; position = 'N'
movements = ['L','M','L','M','L','M','M']
movements_2 = ['M','M','R','M','M','R','R','M']

positions = {'N':{'R':'E','L':'W'}, 'S':{'R':'W','L':'E'}, 'W':{'R':'N','L':'S'}, 'E':{'R':'S','L':'N'}}

def robot(x, y, pos, movs):
	for i in movs:
		if i == 'M':
			if pos == 'N':
				y+=1
			elif pos == 'W':
				x-=1	
			elif pos == 'S':
				y-=1	
			elif pos == 'E':
				x+=1	
		else:
			pos = positions[pos][i]
	return f"{x}, {y} {pos}"

robotic = robot(x, y, position, movements)

print(robotic)