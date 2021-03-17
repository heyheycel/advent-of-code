instructions = []
with open('day4_input.txt') as f:
    for line in f:
    	instructions.append(line)

count=0
for line in instructions:
	valid=True
	for word in line.split():
		if (line.split().count(word) > 1):
			valid = False
			break
	if (valid):
		count+=1


print(count)



#part 2
def sortWords(lista):
	sortList=[]
	for word in lista:
		sortWord=''.join(sorted(word))
		sortList.append(sortWord)

	return sortList



invalid=0
for line in instructions:
	valid=True
	sortList=sortWords(line.split())
	for word in sortList:
		if (sortList.count(word) > 1):
			valid = False
			break
	if (valid):
		invalid+=1


print(invalid)









