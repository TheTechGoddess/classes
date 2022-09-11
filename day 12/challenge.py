x = 1
y = 2
pos = 'N'


def mov_E():
	z+=1

def mov_W():
	z-=1

def mov_N():
	y+=1

def mov_S():
	y-=1	



def north(x):
	if x == 'L':
		pos = 'W'
	elif x == 'R':
		pos = 'E'
	elif x == 'M':
		mov_N()		

def south(x):
	if x == 'L':
		pos = 'E'
	elif x == 'R':
		pos = 'W'
	elif x == 'M':
		mov_S()

def east(x):
	if x == 'L':
		pos = 'N'
	elif x == 'R':
		pos = 'S'
	elif x == 'M':
		mov_E()	

def west(x):
	if x == 'L':
		pos = 'S'
	elif x == 'R':
		pos = 'N'
	elif x == 'M':
		mov_W()			

def move(moves):
	for i in moves:
		if pos == 'N':
			north(i)
			continue	

		if pos == 'E':
			east(i)
			continue	
						
		if pos == 'W':
			west(i)
			continue	
								
		if pos == 'S':
			south(i)
			continue	

move(['L','M','R','R'])

											