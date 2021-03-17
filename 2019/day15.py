from intcode_class3 import Computer
from collections import OrderedDict
import os
import pdb



def list_op():
    opcodes=[]
    with open('input_day15.txt') as f:
        for line in f:
            for op in line.strip().split(','):
                opcodes.append(int(op))
    return opcodes


code = list_op()

#program = Computer(code)
#program.set_input_data(1)
#print(program.calculate())


class Droid:
	wall=0
	ok=1
	target=2
	unexplored=3

	north=1
	south=2
	west=3
	east=4

	def __init__(self,m):
		self.m=m
		self.program=Computer(self.m)
		self.history=[]
		
		self.bounds=(0,0,0,0)
		self.pos=(0,0)
		self.tank_pos=None
		self.move_count=0
		self._map=OrderedDict({(0,0):Droid.ok})
		self.tiles={
		0:'#',
		1:'.',
		2:'*'
		}



	def reset(self):
		if not self._map: return
		self.pos=(0,0)
		self.move_count=0
		self.tank_pos=None

		self._map=OrderedDict()
		self.program=Computer(self.m)


	def map(self, display=True):
		self.reset()

		program=self.program
		history=self.history
		p=self.pos=(0,0)
		possible_moves=set(range(1,5))
		move=self.north
		#tries: the position already tried and with which move
		tries={p:{self.reverse(self.north)}}
		#tries={p:{self.north}}
		#print("tries "+str(tries))

		while True:
			#print("tries "+str(tries))
			if p not in tries:
				tries[p]={self.reverse(move)}
				#tries[p]={move}

			if len(tries[p])<4:
				backtrack=False

				#next move is the difference between what we can try and we already tried
				#pop() the first one
				move=possible_moves.difference(tries[p]).pop()
				#print("move: "+str(move))
				tries[p].add(move)
			else:
				backtrack=True

				if not history:
					#if there is no more movs to try, then go back to the beggining 
					#print("HERE")
					break
				#move one movement back, even when the position was different
				move=self.reverse(history.pop())
				#move=history.pop()

			program.set_input_data(move)
			output=program.calculate()
			#print("output: "+str(output))
			if output in {self.ok, self.target}:
				p=self.xy(move,p)
				self.pos=p
				self.bounds=self.update_bounds()

				if not backtrack:
					history.append(move)
					self._map[p]=output

				if output ==self.target:
					#calculate the steps it took, the position in where is found
					#try to calculate the shortest path

					self.move_count=len(self.history) if self.move_count==0 else min(self.move_count, len(self.history))
					self.tank_pos=p

			if display:
				self.display()

		return self.tank_pos, self.move_count, self._map


	def reverse(self, direction=None):
		if direction==None: direction=self.history[-1]
		#print("history: "+str(self.history))
		#print("direction "+str(direction))
		'''print({
		self.north:self.south,
		self.south:self.north,
		self.west:self.east,
		self.east:self.west
		}[direction])'''
		return{
		self.north:self.south,
		self.south:self.north,
		self.west:self.east,
		self.east:self.west
		}[direction]


	def xy(self, move, from_xy:tuple=None):
		x, y = from_xy if from_xy else self.pos

		dposible_moves={
		self.north:(0,-1),
		self.south:(0,1),
		self.west:(-1,0),
		self.east:(1,0)
		}
		#to obtain an updated position and the move as output
		#if we are in 0,1 and we need to move to the south then 0,2
		return tuple(a+b for a,b in zip((x,y), dposible_moves[move]))


	def update_bounds(self):
		mxy, xy= list(self.bounds), self.pos
		#get me the min position and the max position from the actual bounds and the actual position
		return tuple([min(p1, p2) for p1, p2 in zip(mxy[:2], xy)] + [max(p1, p2) for p1, p2 in zip(mxy[2:], xy)])


	def display(self):
		minx, miny, maxx, maxy = self.bounds
		maxx, maxy = abs(minx) + maxx, abs(miny) + maxy
		px, py = self.pos

		os.system("cls")

		dash = 'Steps: {}, Max (x): {}, Max (y): {}'.format(len(self.history), maxx, maxy)
		print(dash)
		print('_'*(maxx+1))
		grid = [[' ']*(maxx+1) for _ in range(maxy+1)]
		for (x, y), v in self._map.items():
			x += abs(minx)
			y += abs(miny)

			if x < 0 or x > maxx or y < 0 or y > maxy: break

			try:
				grid[y][x] = self.tiles[v]
			except:
				print('DEBUG', x, y, maxx, maxy)
				exit()
				break

		prev = grid[py+abs(miny)][px+abs(minx)]
		rx, ry = px+abs(minx), py+abs(miny)
		if prev != self.tiles[self.target]:
			grid[ry][rx] = 'o'
		else:
			grid[ry][rx-1] = 'o'
		for l in grid: print(''.join(l))
		print('\n')
		print('_'*(maxx+1))
		print(dash)









r = Droid(code)
tank_pos, steps, rmap = r.map(False)
print('Solution 1:'+str(steps))
#r.map(True)



#solution 2
def neighbours(maps, pos):
	(x, y), adjacent_xy = pos, [(0, -1), (0, 1), (-1, 0), (1, 0)]
	n = [(x + dx, y + dy) for dx, dy in adjacent_xy]
	#print('position '+str(pos))
	#print(n)
	'''for i in n:
		if i in maps:
			print('position in maps '+str(i))
			print('value in maps: '+str(maps.get(i)))'''

	return [npos for npos in n if npos in maps]


def spread(maps, pos, t = 0):
	#pdb.set_trace()
	#print('tiempo: '+str(t))
	if maps.get(pos, Droid.wall) == Droid.wall:
		#print('time with wall: '+str(t-1))
		#print('position with wall: '+str(pos))
		return t - 1

	maps[pos] = Droid.wall
	n = neighbours(maps, pos)
	#print('neighbours: '+str(n))
	#print(max([ spread(maps, npos, t + 1) for npos in n ]))
	return max([ spread(maps, npos, t + 1) for npos in n ])

print('Solution 2:', spread(rmap, tank_pos))


