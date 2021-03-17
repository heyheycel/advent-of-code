mass_list=[]
with open('input_day1.txt') as f:
    for line in f:
    	mass_list.append(int(line))



fuel=0
for mass in mass_list:
	value=mass//3-2
	fuel+=value


print(fuel)


#part 2

def fuel_calculation(mass):
	if mass<9: return 0
	fuel=mass//3-2
	return fuel + fuel_calculation(fuel)



print(sum(fuel_calculation(mass) for mass in mass_list))