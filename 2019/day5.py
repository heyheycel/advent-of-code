
def list_op():
	opcodes=[]
	with open('input_day5.txt') as f:
		for line in f:
			for op in line.strip().split(','):
				opcodes.append(int(op))
	return opcodes



def sol(imput):
	movs={1:4, 2:4, 3:2, 4:2, 7:4, 8:4, 5:3, 6:3}
	opcodes=list_op()
	pointer= 0
	#print(opcodes)
	while True:
		
		#print(pointer)
		opcode=f'{opcodes[pointer]:0>5}'
		#print(opcode)
		
		modei= [digit=='1' for digit in opcode[::-1][2:]]
		opcode=int(opcode[-2:])
		if opcode==99:
			break

		x,y,z=opcodes[pointer+1:pointer+4]
		
		if opcode==3:
			opcodes[x]=imput
		
		else:
			parameter1=(int(modei[0])*x) or (int(not modei[0])* opcodes[x])
			if opcode==4:
				print(f'Salida:{parameter1}')
			else:
				parameter2=(int(modei[1])*y) or (int(not modei[1])* opcodes[y])
				if opcode==1:
					opcodes[z]=parameter1+parameter2
				

				elif opcode==2:
					opcodes[z]=parameter1*parameter2


				elif opcode==5:
					if parameter1!=0:
						pointer = parameter2-movs[opcode]

				
				elif opcode==6:
					if parameter1==0:
						pointer =parameter2-movs[opcode]

				elif opcode==7:
					opcodes[z]=int(parameter1<parameter2)

				elif opcode==8:
					opcodes[z]=int(parameter1==parameter2)

				else:
					print(f'Unkwown opcode, te la pelas {opcode}')

		pointer +=movs[opcode]




		


#part 1
print("Part 1")
sol(1)


#part 2
print("Part 2")
sol(5)
