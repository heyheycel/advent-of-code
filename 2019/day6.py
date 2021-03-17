
with open("input_day6.txt") as f:
	parents={}
	for line in f:
		parent, child=line.strip().split(')')
		parents[child]=parent

sum=0
for node in parents:
	while node in parents:
		node=parents[node]
		sum+=1



print(f'Part 1: {sum}')



#part 2


paths=[['YOU'],['SAN']]


#create the paths to get to YOU and SAN
for path in paths:
	while path[-1] in parents:
		path.append(parents[path[-1]])


for planet0 in range(len(paths[0])):
	node= paths[0][planet0]
	if node in paths[1]:
		planet1=paths[1].index(node)
		print(f'part 2: {planet0+planet1-2}')
		break















