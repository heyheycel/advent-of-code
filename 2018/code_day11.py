import numpy as np
def get_digit(number,position):
	return number//10**position%10

serial_number=6878


def values(x,y):
	rack=(x+1)+10
	power=rack*(y+1)
	power+=serial_number
	power*=rack
	return (power // 100 % 10) - 5

grid=np.fromfunction(values, (6, 6), dtype=int)
print(grid)

X = np.zeros((7, 7), dtype=int)
# Each cell is the sum of every top left grid cell
#sum of values in X and Y
X[1:, 1:] = grid.cumsum(axis=0).cumsum(axis=1)
#print(grid.cumsum()) sum of all the values and is taken into an array
#print(grid.cumsum(axis=0)) sum of values in Y 
#print(grid.cumsum(axis=1)) sum of values in X 
print(X)
size = 3
# Each cell is the sum of the size x size square
tmp = X[size:, size:] + X[:-size, :-size] - X[size:, :-size] - X[:-size, size:]
print(X[size:,size:]) 
print(X[-size, :-size])
print(X[size:, :-size])
print(X[:-size, size:])
print(tmp)
#argmax returns the index of maximum value
print(tmp.argmax())        
x, y = np.unravel_index(tmp.argmax(), tmp.shape)
print("{},{}".format(x+1, y+1))


#part 2
max_sum=0
values=(None,None,None,None)
for i in range(1,7):
	tmp = X[i:, i:] + X[:-i, :-i] - X[i:, :-i] - X[:-i, i:]
	if tmp.max()>max_sum:
		max_sum=tmp.max()
		x, y = np.unravel_index(tmp.argmax(), tmp.shape)
		values= (x+1, y+1, i, max_sum)


print("{},{},{}".format(*values))
