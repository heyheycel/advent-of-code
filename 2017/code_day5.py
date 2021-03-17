instructions = []
with open('day5_input.txt') as f:
    for num in f:
    	instructions.append(int(num))




address = 0
counter = 0

#print(instructions)
while address<len(instructions):
	next = address+instructions[address]
	instructions[address] = instructions[address] + 1
	address = next
	counter =counter+1


print(counter)


memory = []
with open('day5_input.txt') as f:
    for num in f:
    	memory.append(int(num))
address = 0
counter = 0

while address<len(memory):
	next = address+memory[address]
	if memory[address]>2:
		offset = -1
	else:
		offset = 1
	memory[address] = memory[address] + offset
	address = next
	counter+=1
	


print("Second part: " + str(counter))