with open('input_day3.txt') as f:
	cables_lines=[line.strip().split(',') for line in f]

dX={'R':1, 'L':-1, 'U':0, 'D':0}
dY={'R':0, 'L':0, 'U':1, 'D':-1}

visited={0:set(), 1:set()}

for cable in range(2):
	x=y=0
	for cable_line in cables_lines[cable]:
		direction, steps= cable_line[0], int(cable_line[1:])
		for i in range(steps):
			x+=dX[direction]
			y+=dY[direction]
			visited[cable].add((x,y))



intersection = visited[0] & visited[1]



minv=1000000000
for x,y in intersection:
	value= abs(x) +abs(y)
	if value <= minv:
		minv= value

	

print("Solution part 1: "+str(minv))




#part 2





matrix={}	
for cable in range(2):
	x=y=count_steps=0
	for cable_line in cables_lines[cable]:
		direction, steps= cable_line[0], int(cable_line[1:])
		for i in range(steps):
			count_steps+=1
			x+=dX[direction]
			y+=dY[direction]
			position=(x,y)
			if position in matrix:
				if cable not in matrix[position]:
					matrix[position][cable] = count_steps
				if len(matrix[position])>1:
					print("tangled: "+str(position))
					print("count_steps: "+str(matrix[position][0]+matrix[position][1]))
				
			else:
				matrix[position]= {cable:count_steps}



#print(matrix)
for position in matrix.values():
	if len(position) >1:
		print (position)
		print (position[0]+position[1])

min_steps=100000000
for position in matrix.values():
	if len(position) >1:
		value=position[0]+position[1]
		if value<min_steps:
			min_steps=value


#21666
print("Solution part 2: "+str(min_steps))

