from collections import defaultdict
lines = open("input_day14.txt").readlines()
requirements = {}



	
def make_fuel(fuel=1):
	element_needs=defaultdict(int, {'FUEL':fuel})
	element_rest=defaultdict(int)
	ore=0
	print("fuel: "+str(fuel))
	#print(requirements)
	#print(element_needs)
	while element_needs:
		element=list(element_needs.keys())[0]
		if element_needs[element]<=element_rest[element]:
			element_rest[element]-=element_needs[element]
			del element_needs[element]
			continue

		#print("element "+str(element))
		num_needed=element_needs[element]-element_rest[element]
		#print('num_needed '+str(num_needed))
		del element_needs[element]
		del element_rest[element]
		num_produced=requirements[element]['out']
		#print('num_produced '+str(num_produced))

		if (num_needed // num_produced) *num_produced==num_needed:
			num_reactions=num_needed//num_produced
		else:
			num_reactions=(num_needed//num_produced)+1


		element_rest[element]+=(num_reactions*num_produced)-num_needed
		for chem in requirements[element]['in']:
			if chem=='ORE':
				ore+=requirements[element]['in'][chem]*num_reactions

			else:
				#print(element)
				#print(requirements[element])
				element_needs[chem]+=requirements[element]['in'][chem]*num_reactions

	return ore

for line in lines:
	parts = line.strip("\n").replace(",", "").split(" ")
	#print(parts)
	inputs={}
	for i in range((len(parts) - 3)//2):
		#print(parts[i])
		#print(parts[i*2+1])
		#print(parts[i*2])
		inputs[parts[i*2+1]]=int(parts[i*2])
		#print(parts[-1])
		#print(parts[-2])
		requirements[parts[-1]]={'out':int(parts[-2]), 'in': inputs}
		#((int(parts[i*2]), parts[i*2+1]))



#print(requirements)

print('Part 1. Number of ores: '+str(make_fuel()))


#part 2
low=1e12//make_fuel()
high=2*low
#print("ores: "+str(make_fuel(high)))
#print("low: "+str(low))
#print("high: "+str(high))
while make_fuel(high)<1e12:
	#print("ores 2nd: "+str(make_fuel(high)))
	#print("low: "+str(low))
	#print("high: "+str(high))
	low=high
	high=2*low


#print("low: "+str(low))
#print("high: "+str(high))
while low < high - 1:
    mid = (low + high) // 2
    #print("mid "+str(mid))
    ore = make_fuel(mid)
    #print("ore "+str(ore))
    #print("low: "+str(low))
    #print("high: "+str(high))
    #how much ore is needed for that fuel until we reach equals to 1e12
    if ore < 1e12:
        low = mid
    elif ore > 1e12:
        high = mid
    else:
    	#1e12
        break

print("Part 2: " +str(int(mid)))




