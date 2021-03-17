#to convert lines to 0's anc 1's for plants
def string_to_list(line):
     return [int(c == "#") for c in line]

def list_to_string(lista):
     return "".join(["#" if x else "." for x in lista])
import numpy as np

s=open('input_day12.txt')
lines = s.readlines()
#number 2 because of the initial state words added at the beggining
previous_garden = lines[0].split()[2]
previous_garden= string_to_list(previous_garden)
current_garden=previous_garden
print(current_garden)
instructions={}
negatives=0
for i in range(2, len(lines)):
     before, after = lines[i].split(" => ")
     instructions[before] = int(after.strip('\n') == "#")
     #instructions[before]=after.strip('\n')

print(instructions)


for gen in range(200):
     previous_garden=[0]*5+previous_garden+[0]*5
     current_garden=[0]*5+current_garden+[0]*5
     negatives+=5
     print(list_to_string(previous_garden))
     for i in range(2,len(previous_garden)-3):
          pattern = list_to_string(previous_garden[i - 2 : i + 3])
          #print(pattern)
          current_garden[i] = instructions[pattern] if pattern in instructions else 0
     
     current_garden = np.trim_zeros(current_garden, "f")
     negatives -= len(previous_garden) - len(current_garden)
     #print(previous_garden)
     #print(current_garden)
     #print(len(previous_garden)-len(current_garden))
     #print(negatives)
     current_garden=np.trim_zeros(current_garden,"b")
     previous_garden=current_garden


resultado=0
for i in range(len(current_garden)):
     if current_garden[i]:
          resultado+=i-negatives

print(resultado)






previous = lines[0].split()[2]
previous = string_to_list(previous)
current = previous
patterns = {}
negatives = 0
for i in range(2, len(lines)):
    before, after = lines[i].split(" => ")
    patterns[before] = int(after.strip('\n') == "#")


for gen in range(50000000000):
    prev_negatives = negatives
    previous = [0] * 5 + previous + [0] * 5
    current = [0] * 5 + current + [0] * 5
    negatives += 5
    print(list_to_string(previous_garden))
    for i in range(2, len(previous) - 3):
        pattern = list_to_string(previous[i - 2 : i + 3])
        current[i] = patterns[pattern] if pattern in patterns else 0
    current = np.trim_zeros(current, "f")
    negatives -= len(previous) - len(current)
    current = np.trim_zeros(current, "b")
    previous = np.trim_zeros(previous)
    if np.array_equal(previous, current):
        diff_negatives = negatives - prev_negatives
        negatives += diff_negatives * (50000000000 - gen - 1)
        break
    previous = current

        
resultado = 0
for i in range(len(current)):
    if current[i]:
        resultado += i - negatives

print("Part 2: "+str(resultado))




















