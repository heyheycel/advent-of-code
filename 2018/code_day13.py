with open('input_day13.txt') as f:
    lines=f.read().splitlines()



class Car:
	def __init__(self, x,y,direction,next_turn,id_car):
		self.x=x
		self.y=y
		self.direction=direction
		self.next_turn=next_turn
		self.id=id_car
	



world=[]
cars=[]
rail_chars = "|\/+-"
char_to_int={" ":0}
char_to_int.update({char: 1 for char in rail_chars})
char_to_int.update({
"|": 1,
"\\": 2,
"/": 3,
"+": 4,
"-": 5,
"v": 11,
"<": 15,
"^": 11,
">": 15,
})
car_char_to_dir = {"v": 3, "<": 0, "^": 1, ">": 2}

print(len(lines))
print(lines)
count=0
for y in range(len(lines)):
	row=[]
	for x in range(len(lines[y])):
		#print("y, x "+str(y)+" "+str(x))
		char=lines[y][x]
		#print(char)
		row.append(char_to_int[char])
		if char in car_char_to_dir.keys():
			cars.append(Car(x,y,car_char_to_dir[char],0,count))
			count+=1
			#print(Car)
	world.append(row)

print(world)
#print(cars)
a=True
while a:
	cars.sort(key=lambda car: (car.y, car.x))
	for car in cars:
		x, y = car.x, car.y
		print("y, x "+str(y)+" "+str(x))
		#print(world[y][x])
		#it is \
		if world[y][x]%10==2:
			if car.direction==0:
				car.direction=1
			elif car.direction==1:
				car.direction=0
			elif car.direction==2:
				car.direction=3
			elif car.direction==3:
				car.direction=2
		#it is /		
		if world[y][x] % 10 == 3:
			if car.direction == 0:
				car.direction = 3
			elif car.direction == 1:
				car.direction = 2
			elif car.direction == 2:
				car.direction = 1
			elif car.direction == 3:
				car.direction = 0
		#it is +			
		if world[y][x] % 10 == 4:
			if car.next_turn == 0:
				car.direction = (car.direction - 1) % 4
			elif car.next_turn == 2:
				car.direction = (car.direction + 1) % 4
			car.next_turn = (car.next_turn + 1) % 3	


		if car.direction == 0:
			car.x -= 1
		elif car.direction == 1:
			car.y -= 1
		elif car.direction == 2:
			car.x += 1
		elif car.direction == 3:
			car.y += 1

		if world[car.y][car.x] >= 10:
			print("Crash: {},{}".format(car.x, car.y))
			a=False

		#updates matriz
		world[y][x] -= 10
		world[car.y][car.x] += 10





#part 2
world=[]
cars=[]
print(len(lines))
print(lines)
count=0
for y in range(len(lines)):
	row=[]
	for x in range(len(lines[y])):
		#print("y, x "+str(y)+" "+str(x))
		char=lines[y][x]
		#print(char)
		row.append(char_to_int[char])
		if char in car_char_to_dir.keys():
			cars.append(Car(x,y,car_char_to_dir[char],0,count))
			count+=1
			#print(Car)
	world.append(row)

print(world)
#print(cars)
a=True
to_remove=[]
while a:
	cars.sort(key=lambda car: (car.y, car.x))
	for car in cars:
		print("Cars len begin: "+str(len(cars)))
		print("car pos "+str(car.x)+" "+str(car.y))
		print("car id: "+str(car.id))
		print("To remove begin: "+str(to_remove))
		if car.id in to_remove:
			continue
		x, y = car.x, car.y
		if len(cars)==2 and car.id not in to_remove:
			break
		print("y, x "+str(y)+" "+str(x))
		#print(world[y][x])
		#it is \
		if world[y][x]%10==2:
			if car.direction==0:
				car.direction=1
			elif car.direction==1:
				car.direction=0
			elif car.direction==2:
				car.direction=3
			elif car.direction==3:
				car.direction=2
		#it is /		
		if world[y][x] % 10 == 3:
			if car.direction == 0:
				car.direction = 3
			elif car.direction == 1:
				car.direction = 2
			elif car.direction == 2:
				car.direction = 1
			elif car.direction == 3:
				car.direction = 0
		#it is +			
		if world[y][x] % 10 == 4:
			if car.next_turn == 0:
				car.direction = (car.direction - 1) % 4
			elif car.next_turn == 2:
				car.direction = (car.direction + 1) % 4
			car.next_turn = (car.next_turn + 1) % 3	


		if car.direction == 0:
			car.x -= 1
		elif car.direction == 1:
			car.y -= 1
		elif car.direction == 2:
			car.x += 1
		elif car.direction == 3:
			car.y += 1


		world[y][x] -= 10
		if world[car.y][car.x] >= 10:
			print("Crash Part 2: {},{}".format(car.x, car.y))
			to_remove.append(car.id)
			for tmp_car in cars:
				if tmp_car.x==car.x and tmp_car.y==car.y and tmp_car.id!=car.id:
					world[tmp_car.y][tmp_car.x]-=10
					to_remove.append(tmp_car.id)
					break
			
		else:
			world[car.y][car.x] += 10  
	

	
	if len(to_remove)>0:
		print("To remove: "+str(to_remove))
		print("len before: "+str(len(cars)))
		tmp_cars=cars
		for car in cars:
			print("Car POS: "+str(car.x)+","+str(car.y))
			if car.id in to_remove:
				print("Car to remove: "+str(car.id))
				to_remove.remove(car.id)
				tmp_cars.remove(car)

		cars=tmp_cars
		print("len after: "+str(len(cars)))
		print("To remove: "+str(to_remove))


	if len(cars)<=1:
		a=False    
		break


print("{},{}".format(cars[0].x, cars[0].y))
print("Car id: "+str(cars[0].id))
print(cars[0].direction)



















#https://github.com/badouralix/advent-of-code-2018/blob/master/day-13/part-1/thomas.py