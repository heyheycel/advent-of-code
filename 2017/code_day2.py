instructions = []
differences=[]
with open('day2_input.txt') as f:
    for line in f:
    	instructions.append([int(i) for i in line.split()])

def smaller(lista):
	tmp=lista[0]
	for i in range(1,len(lista)):
		if tmp>lista[i]:
			tmp=lista[i]
	return tmp


def bigger(lista):
	tmp=lista[0]
	for i in range(1,len(lista)):
		if tmp<lista[i]:
			tmp=lista[i]
	return tmp

def divisible(lista):
	second=0
	for a in lista:
		for b in lista:
			if a % b == 0 and a != b:
				second += a // b
	return second


#part 1
second=0
for row in instructions:
	small=smaller(row)
	big=bigger(row)
	res=big-small
	differences.append(res)
	#part 2
	second+=divisible(row)

print(sum(differences))
print(second)







