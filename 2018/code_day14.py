recipes = [3, 7]
duendes= [0, 1]
longitud=323081
#longitud=5
while len(recipes) < longitud + 10:
	new = recipes[duendes[0]] + recipes[duendes[1]]
	recipes += [int(c) for c in str(new)]
	duende1=(duendes[0]+1+recipes[duendes[0]])%len(recipes)
	duende2=(duendes[1]+1+recipes[duendes[1]])%len(recipes)
	duendes= [duende1,duende2]
	#print(recipes)

print("Part 1:")   
print("".join(str(n) for n in recipes[longitud : longitud + 10]))



#part 2
puzzle_input =str(longitud)
recipes = [3, 7]
duendes = [0, 1]
input_found = None
while input_found is None:
	actual = ''.join(str(e) for e in recipes[-len(puzzle_input) - 1 : -1])
	actual2= ''.join(str(e) for e in recipes[-len(puzzle_input): -1])
	#print(actual)
	#print(actual2)
	if actual==puzzle_input:
		input_found = -len(puzzle_input) - 1
		break
	if actual2==puzzle_input:
		input_found = -len(puzzle_input)
		break
	new = recipes[duendes[0]] + recipes[duendes[1]]
	recipes += [int(c) for c in str(new)]
	duende1=(duendes[0]+1+recipes[duendes[0]])%len(recipes)
	duende2=(duendes[1]+1+recipes[duendes[1]])%len(recipes)
	duendes= [duende1,duende2]

print(input_found)
print("Part 2: "+str(len(recipes) + input_found))