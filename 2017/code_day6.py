#import pdb
input = [int(x) for x in open('day6_input.txt', 'r').read().split("\t")]


def redistribute(lista):
	index=lista.index(max(lista))
	value=lista[index]
	lista[index]=0
	n=len(lista)
	for i in range(index+1,index+value+1):
		lista[i % n] += 1

	return lista


def returnKey(lista):
	return','.join(str(num) for num in lista)

count=1
index=1
seenLists={returnKey(input):index}
#pdb.set_trace()
while (True):
	lista=redistribute(input)
	if returnKey(lista) not in seenLists:
		count+=1
		index+=1
		seenLists[returnKey(lista)]=index
	else:
		index+=1
		print(index)
		lastList=seenLists[returnKey(lista)]
		print(seenLists[returnKey(lista)])
		print("Second answer "+str(index-lastList))
		break

print("First answer " +str(count))







