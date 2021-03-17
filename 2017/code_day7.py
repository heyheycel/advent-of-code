with open("day7_input.txt", "r") as arch:
	data = arch.read().strip().split('\n')



class Node:
	def __init__(self, value, children):
		self.value = value
		self.children = children
		self.indegree = 0

nodes = {}

for line in data:
	name = line.split(' ')[0]
	value = int(line.split('(')[1].split(')')[0])
	children = []
	if len(line.split('->')) > 1:
		children = line.split('->')[1].replace(' ', '').split(',')
	nodes[name] = Node(value, children)
	#print(name)
	#print(str(nodes[name].children) + str(nodes[name].value)+ str(nodes[name].indegree))


for node in nodes.values():
	for child in node.children:
		nodes[child].indegree += 1
		#print(nodes[child].indegree)


for key in nodes:
	if nodes[key].indegree == 0:
		root=key
		print (root)


#part 2


def getDifferentNode(vals):
	uniques={}
	for number in vals:
		if number in uniques:
			uniques[number]+=1
		else:
			uniques[number]=1
	for val in uniques.keys():
		if uniques[val]==1:
			return val


	

def getCommonNode(vals):
	uniques={}
	for number in vals:
		if number in uniques:
			uniques[number]+=1
		else:
			uniques[number]=1
	for val in uniques.keys():
		if uniques[val]>1:
			return val

def visit(name):
	vals = [visit(x) for x in nodes[name].children]
	if (len(set(vals))>1):
		print(vals)
		print(getDifferentNode(vals))
		print(getCommonNode(vals))
		least_common=getDifferentNode(vals)
		most_common=getCommonNode(vals)
		child_val = nodes[nodes[name].children[vals.index(least_common)]].value
		print(child_val)
		print("Node should be: "+str(most_common-least_common+child_val))
	return sum(vals) + nodes[name].value




visit(root)	






















