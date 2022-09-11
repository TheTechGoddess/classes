N = 6
start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
i=0
meeting = []
count=1

while i<N:
	meeting.append([start[i],end[i]])
	i+=1
	print(meeting)
	if start[i]<start[i+1]:
		

	