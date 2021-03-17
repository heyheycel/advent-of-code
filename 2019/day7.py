from itertools import permutations
from intcode_class import Intcode

def list_op():
	opcodes=[]
	with open('input_day7.txt') as f:
		for line in f:
			for op in line.strip().split(','):
				opcodes.append(int(op))
	return opcodes



def sol(opcodes,phase,imput):
	movs={1:4, 2:4, 3:2, 4:2, 7:4, 8:4, 5:3, 6:3}
	inputCount = 0
	#opcodes=list_op()
	pointer= 0
	#print(opcodes)
	#print(opcodes)
	#print(phase)
	#print("inputCount")
	#print(inputCount)
	while True:
		#print(pointer)
		opcode=f'{opcodes[pointer]:0>5}'
		#print(opcode)
		
		modei= [digit=='1' for digit in opcode[::-1][2:]]
		opcode=int(opcode[-2:])
		if opcode==99:
			return parameter1
			break

		x,y,z=opcodes[pointer+1:pointer+4]
		
		#take an input value
		if opcode==3:
			if(inputCount == 0):
				choice = phase
				inputCount += 1
			else:
				choice = imput

			opcodes[x]=choice
           
            
		
		else:
			parameter1=(int(modei[0])*x) or (int(not modei[0])* opcodes[x])

			#return an output value
			if opcode==4:
				#print(f'Salida:{parameter1}')
				returnValue = parameter1
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
	return returnValue



#part 1
perms = list(permutations(range(5)))
for i in range(len(perms)):
    perms[i] = list(perms[i])
 
max_output = 0
file1 = list_op()
 
for a,b,c,d,e in perms:
	#sol recibe 3 valores, reset del codigo, la phase donde va y el input que le da el valor anterior 
    output = sol(file1,e,sol(file1,d,sol(file1,c,sol(file1,b,sol(file1,a,0)))))
    if(output>max_output):
        max_output = output


print("Max output " + str(max_output))




#part 2


perms = list(permutations(range(5,10)))
for i in range(len(perms)):
    perms[i] = list(perms[i])
 
maxOutput = 0
file1 = list_op()
 
for x in perms:
	amp1 = Intcode("Amplifier 1", file1, x[0], 0)
	amp2 = Intcode("Amplifier 2", file1, x[1], 0)
	amp3 = Intcode("Amplifier 3", file1, x[2], 0)
	amp4 = Intcode("Amplifier 4", file1, x[3], 0)
	amp5 = Intcode("Amplifier 5", file1, x[4], 0)

	output = 0

	
	while(amp5.getCode() != 99):
		#print("getcode " +str(amp5.getCode()))
		output = amp5.codeRun(amp4.codeRun(amp3.codeRun(amp2.codeRun(amp1.codeRun(output)))))
		#output=amp5.codeRun(output)
		if(output != None):
			if(output>maxOutput):
				maxOutput = output


print("Maxoutput part 2 " + str(maxOutput))