import math
archive=open('input_day10.txt').read().split()
#print(archive)


def get_monitoring_station(coordinates):
	max_asteroids = 0
	best_x = best_y = 0
	for x, y in coordinates:
		#print("X,Y: "+str(x)+","+str(y))
		slopes = set()
		for x2, y2 in coordinates:
			if (x, y) != (x2, y2):
				#find the distance
				dx, dy = x2 - x, y2 - y
				#reduce the distance by dividing into greatest comun divisor
				dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
				#The number of different tuples is the number of visible asteroids.
				slopes.add((dx, dy))
				#print(slopes)
		if len(slopes) > max_asteroids:
			max_asteroids = len(slopes)
			best_x, best_y = x, y

	return max_asteroids, (best_x, best_y)







map_coordinates=[]
for y, row in enumerate(archive):
	for x, value in enumerate(row):
		if value=="#":
			map_coordinates.append((x,y))

#asteroid_coordinates = [(x, y) for y, row in enumerate(archive) for x, value in enumerate(row) if value == '#']
#print(map_coordinates)
#print(asteroid_coordinates)
#map_coordinates=((1,0),(4,0),(0,2),(1,2),(2,2),(3,2),(4,2),(4,3),(3,4),(4,4))
#numero de asteroides que puede ver - coordenadas de este
print("Part 1: "+str(get_monitoring_station(map_coordinates)))

number_asteroids, coordinates_p = get_monitoring_station(map_coordinates)


#angle between two points
def get_angle(start, end):
	result = math.atan2(end[0] - start[0], start[1] - end[1]) * 180 / math.pi
	if result < 0:
		return 360 + result
	return result



list_coordinates=list(map_coordinates)
list_coordinates.remove(coordinates_p)
part2_coordinates=tuple(map_coordinates)


list_angles=[]
for end in part2_coordinates:
	angle=get_angle(coordinates_p,end)
	list_angles.append((angle,end))

#sort the angles by the distance with the point 
angles=sorted(list_angles, key=lambda x: (x[0], abs(coordinates_p[0] - x[1][0]) + abs(coordinates_p[1] - x[1][1])))

#shooting the first angle
idx = 0
last = angles.pop(idx)
last_angle = last[0]
count=1

while count < 200 and angles:
	#if we are at the end of the circle
	if idx >= len(angles):
		idx = 0
		last_angle = None

	if last_angle == angles[idx][0]:
		idx += 1
		continue
	last = angles.pop(idx)
	last_angle = last[0]
	count += 1

print ('vaporized {}: {} {}'.format(count, last[1], last[1][0] * 100 + last[1][1]))








