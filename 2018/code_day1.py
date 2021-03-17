import itertools
instructions=[]
with open('input_day1.txt') as f:
    for line in f:
    	instructions.append(int(line))


#instructions=[+1, -2, +3,+1,+1,-2]
freq=0
frequencies=set([0])
for i in instructions:
	freq+=i

print(freq)

freq2=0
for num in itertools.cycle(instructions):
    freq2 += num
    if freq2 in frequencies:
        print(freq2); break
    frequencies.add(freq2)




