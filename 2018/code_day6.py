
#353X
#358Y

data=[]
for line in open('input_day6.txt').readlines():
	coord = tuple(map(int, line.split(', ')))
	data.append(coord)


max_x=max(data, key=lambda x:x[0])[0]
max_y=max(data, key=lambda x:x[1])[1]

grid={}
for i in range(max_x+1):
	for j in range(max_y+1):
		#of all the coords given, give me the one that is closest, and give the manhatan distance to it
		 min_value = min(abs(i-x)+abs(j-y) for x, y in data)
		 #print(min_value)
		 for n, (x,y) in enumerate(data):
		 	if abs(i-x)+abs(j-y) == min_value:
		 		#if value was already chossen put a -1 
		 		if grid.get((i, j), -1) != -1:
		 			grid[i, j] = -1
		 			break
		 		grid[i, j] = n



#for counter, value in enumerate(data):
    #print(counter, value)

#for key, value in grid.items():
	#print(str(key)+str(value))


def getMaxValue(grid, infinite):
	common={}
	for value in grid.values():
		if common.get(value)==None:
			common[value]=0
		common[value]+=1
	max_value=0
	for key, value in common.items():
		if value>max_value and key not in infinite:
			max_value=value
	return max_value



corners = set([-1])
#esquinas con el maximo de Y 
corners = corners.union(set(grid[x, max_y] for x in range(max_x)))
#esquinas con el minimo de Y, en este caso 0
corners = corners.union(set(grid[x,0] for x in range(max_x)))
#esquinas con el minimo de X, en este caso desde 0
corners = corners.union(set(grid[max_x, y] for y in range(max_y)))
#esquinas con el maximo de X
corners = corners.union(set(grid[0, y] for y in range(max_y)))
print(corners)

#part 1
max_value=getMaxValue(grid,corners)
print(max_value)

#part 2
valid_sums=[]
for i in range(max_x+1):
	for j in range(max_y+1):
		suma=0
		for x,y in data:
			suma+=(abs(i-x)+abs(j-y))
		
		if suma<10000:
			valid_sums.append(suma)
				
		
print(len(valid_sums))
