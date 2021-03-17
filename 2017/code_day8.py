import re

with open("day8_input.txt", "r") as arch:
	input = arch.read().strip().split('\n')


operations = {">":lambda x,v: x>v,"<":lambda x,v: x<v, "inc":lambda x,v: x+v,"<=": lambda x,v: x<=v, "!=": lambda x,v: x!=v, ">=": lambda x,v: x>=v, "==": lambda x,v: x==v, "dec":lambda x,v: x-v}

registers={}

max_value=0
for line in input:
	instruction=re.match("([a-z]+)\s(inc|dec)\s(-?\d+)\sif\s([a-z]+)\s(<|>|!=|==|>=|<=)\s(-?\d+)",line)
	register=instruction.group(1)
	inc_dec=instruction.group(2)
	value=int(instruction.group(3))
	condition_register=instruction.group(4)
	condition=instruction.group(5)
	condition_inc=int(instruction.group(6))

	if register not in registers:
		registers[register]=0
	if condition_register not in registers:
		registers[condition_register]=0
	if operations[condition](registers[condition_register], condition_inc):
		registers[register]=operations[inc_dec](registers[register], value)
		if registers[register] > max_value:
			max_value = registers[register]

print(registers)

numbers=[]
for number in registers.values():
	numbers.append(number)
print(numbers)
print(max(numbers))
print(max_value)


































