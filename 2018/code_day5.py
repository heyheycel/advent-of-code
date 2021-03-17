import pdb
with open("input_day5.txt", "r") as f:
	string=f.read().strip()



#string="abAcCaCBAcCca"
alphabet="abcdefghijklmnopqrstuvwxyz"




def part1(string):
	tmp=None
	while tmp != string:
		tmp = string
		for i in alphabet:
			string =string.replace(i.upper() +i.lower(),"")
			string = string.replace(i.lower() +  i.upper(),"")
	return string



print(len(part1(string)))


def part2(string):
	tmp=""
	value=len(string)
	for i in alphabet:
		tmp=string.replace(i,"").replace(i.upper(),"")
		#print(tmp)
		length=len(part1(tmp))
		value = length if length < value else value
	return value

print(part2(string))

