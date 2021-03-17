from re import findall
from functools import reduce
from math import gcd

def extract_ints(line):
    return [int(x) for x in findall(r'-?\d+', line)]


def apply_gravity(positions, velocities):
    for moon1 in range(3):
        for moon2 in range(moon1+1, 4):
            for dim in range(3):
                if positions[moon1][dim] > positions[moon2][dim]:
                    velocities[moon1][dim] -= 1
                    velocities[moon2][dim] += 1
                elif positions[moon1][dim] < positions[moon2][dim]:
                    velocities[moon1][dim] += 1
                    velocities[moon2][dim] -= 1


def apply_velocity(positions, velocities):
    for moon in range(4):
        for dim in range(3):
            positions[moon][dim] += velocities[moon][dim]


def calculate_energy(positions, velocities):
    total_energy = 0
    for i in range(4):
        potential = sum([abs(moon) for moon in positions[i]])
        kinectic = sum([abs(velocity) for velocity in velocities[i]])
        total_energy += potential * kinectic
    return total_energy


positions=[]
with open('input_day12.txt') as f:
    for line in f:
        positions.append(extract_ints(line))

velocities  = [[0 for x in range(3)] for y in range(4)]
print(positions)
print(velocities)

for x in range(1000):
    apply_gravity(positions, velocities)
    apply_velocity(positions, velocities)

print(positions)
print(velocities)
print("P1: "+str(calculate_energy(positions,velocities)))



#part2

def apply_gravity2(positions, velocities):
    for moon1 in range(3):
        for moon2 in range(moon1+1, 4):
                #print(positions[moon1])
                #print(positions[moon2])
                if positions[moon1] > positions[moon2]:
                    velocities[moon1] -= 1
                    velocities[moon2] += 1
                elif positions[moon1] < positions[moon2]:
                    velocities[moon1] += 1
                    velocities[moon2] -= 1


def apply_velocity2(positions, velocities):
    for moon in range(4):
            positions[moon] += velocities[moon]

def matches_start_state(positions, velocities, positions_new, velocities_new, dim):
    #print("matches_start_state")
    #print(positions)
    #print(velocities)
    for i in range(4):
        if positions[i][dim] != positions_new[i] or \
           velocities[i][dim] != velocities_new[i]:
            return False
    return True


def least_common_multiple(a,b):
    if a>b:
        greater=a
    else:
        greater=b

    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1

    return lcm

def greatest_common_divisor(a,b): 
      
    # Everything divides 0  
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
  
    # base case 
    if (a == b): 
        return a 
  
    # a is greater 
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 

def calculate_lcm(steps):
    return reduce(least_common_multiple, steps)

def calculate_lcm2(steps):
    return reduce(lambda a,b: a*b // greatest_common_divisor(a,b), steps)


positions=[]
with open('input_day12.txt') as f:
    for line in f:
        positions.append(extract_ints(line))

velocities  = [[0 for x in range(3)] for y in range(4)]
print(positions)
print(velocities)

steps=[0,0,0]

for i in range(3):
    positions_new=[position[i] for position in positions]
    velocities_new=[velocity[i] for velocity in velocities]
    #print(positions_new)
    #print(velocities_new)
    while True:
        apply_gravity2(positions_new,velocities_new)
        apply_velocity2(positions_new,velocities_new)

        steps[i]+=1
        #if matches_start_state(positions, velocities, positions_new, velocities_new,i):
            #print("match")
            #print(positions)
            #print(velocities)
            #print(positions[i]) 
            #print(velocities[i])
            #print(positions_new)
            #print(velocities_new)
        if matches_start_state(positions, velocities, positions_new, velocities_new, i):
            break

#print(positions_new)
#print(velocities_new)
#print(positions)
#print(velocities)
print(steps)
print("P2: "+str(calculate_lcm2(steps)))





