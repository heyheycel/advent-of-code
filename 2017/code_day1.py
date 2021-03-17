with open('captcha1.txt') as f:
	instructions = f.readline()


nums = list(map(int, instructions))
def solve(lista, mode):
	sumas=[]
	if mode==1:
		jump=1
	else:
		jump=len(lista)//2
	for i in range(len(lista)):
		if lista[i]==lista[i-jump]:
			sumas.append(lista[i])
	return sumas
#part 1
print(sum(solve(nums,1)))
#part 2
print(sum(solve(nums,0)))