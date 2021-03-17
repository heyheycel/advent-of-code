from collections import deque


def solve(inputs):
	for phase in range(100):
		for pos in range(len(inputs)):
			#deque to move the elements with rotate
			pattern=deque([p for p in [0,1,0,-1] for _ in range(pos+1)])
			#print("pattern "+str(pattern))
			#take the first element and put it in the last position
			pattern.rotate(-1)
			#print("pattern rotated "+str(pattern))
			result=0
			for i in range(len(inputs)):
				result+=inputs[i]*pattern[0]
				#print("result "+str(inputs[i]*pattern[0]))
				#para mover el valor de ahorita al final y tener en la posicion 0 al siguiente valor
				pattern.rotate(-1)
				#print("pattern rotated "+str(pattern))

			print(result)
			inputs[pos]=abs(result)%10
			#print("here "+str(inputs[pos]))
			print(inputs)

			#print(inputs)

	

	return "".join(str(x)for x in inputs[:8])


	



main_list=[0,3,0,3,6,7,3,2,5,7,7,2,1,2,9,4,4,0,6,3,4,9,1,5,6,5,4,7,4,6,6,4]

#line=open("input_day16.txt","r").readline()
#for i in line:
	#main_list.append(int(i))

#print(main_list)
part1=solve(main_list)
#print("Solution of part1: "+str(part1))

#main_string = open("input_day16.txt").read()*10000
main_string='1111111111'
#print(main_string[0:7])
temp_elements = (main_string[int(main_string[0:7]):])
main_elements=[]
for i in temp_elements:
	main_elements.append(int(i))
#print(main_elements)
def part2(main_elements):
	for _ in range(100):
		for i in range(-2, -len(main_elements)-1, -1):
			print(main_elements)
			print(main_elements[-2])
			print(main_elements[i+1])
			print("pos "+str(i))
			main_elements[i] = (main_elements[i] + main_elements[i+1]) % 10
	return "".join([str(x) for x in main_elements[:8]])

#print(part2(main_elements))