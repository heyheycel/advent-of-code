

instructions = []
with open('input_day2.txt') as f:
    for line in f:
    	instructions.append(line.strip())



def numberOfTwo(letters):
	for  i in letters.values():
		if i ==2:
			return 1
	return 0

def numberOfThree(letters):
	for  i in letters.values():
		if i ==3:
			return 1
	return 0


twos=0
threes=0
for line in instructions:
	letter_count={}
	for letter in line:
		if letter in letter_count:
			letter_count[letter]+=1
		else:
			letter_count[letter]=1
	twos+=numberOfTwo(letter_count)
	threes+=numberOfThree(letter_count)

print(twos)
print(threes)
print("Part 1: "+str(twos*threes))




for word1 in instructions:
	for word2 in instructions:
		diff = 0
		for i in range(len(word1)):
			if word1[i] != word2[i]:
				diff += 1
				if diff>1:
					break;
		if diff == 1:
			ans = []
			for i in range(len(word1)):
				if word1[i] == word2[i]:
					ans.append(word1[i])
			print (''.join(ans))
			print (word1,word2)