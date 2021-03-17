
def list_op():
	opcodes=[]
	with open('input_day2.txt') as f:
		for line in f:
			for op in line.strip().split(','):
				opcodes.append(int(op))
	return opcodes



def sol(noun, verb):
	opcodes=list_op()
	opcodes[1], opcodes[2], pointer= noun, verb, 0

	while True:
		opcode=opcodes[pointer]
		if opcode==99:
			break

		elif opcode==1:
			idx1,idx2,idx3=opcodes[pointer+1:pointer+4]
			opcodes[idx3]=opcodes[idx1]+opcodes[idx2]
			pointer+=4
		elif opcode==2:
			idx1,idx2,idx3=opcodes[pointer+1:pointer+4]
			opcodes[idx3]=opcodes[idx1]*opcodes[idx2]
			pointer+=4
		else:
			print("Te la pelas, ese no lo leo: "+str(opcode))

	return opcodes[0]



print(sol(12,2)) 


#part 2
expected=19690720
for noun in range(100):
	for verb in range(100):
		result=sol(noun,verb)

		if result==expected:
			print("Part 2: "+ str(100 * noun + verb))
			break







