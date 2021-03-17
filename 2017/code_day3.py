

num=265149
current=1
level=0
while current<num:
	level+=1
	current=current+level*8

print("Given number: "+str(num))
print("Number of cells: "+str(current))
print("Number of shells in the square: "+str(level))
distance=current-num
print("Distance from the last cell to the given cell: "+str(distance))
"""
side one (last cell): (2k+1)^2
side two (half of last cell): (2k+1)^2-K
side three (bottom left side): (2k+1)^2-2K
side four (half of bottom left side): (2k+1)^2-3K
side five (upper left side): (2k+1)^2-4K
side six (half upper left side): (2k+1)^2-5K
side seven (upper right): (2k+1)^2-6K
side eight (half upper right): (2k+1)^2-7K 

"""





sideTwo=((2*level+1)**2)-level
print("Print half of the last axis: "+str(sideTwo))
distanceSideTwo=num-sideTwo
print("Print distance from half to the number: "+str(distanceSideTwo))
distanceFromCenter=distanceSideTwo+level
print("Distance from center: "+str(distanceFromCenter))
rootSquare=current**(.5)
print("Long of the line of the square: "+str(rootSquare))





#Part 2




def left(x, y): return (x - 1, y)
def right(x, y): return (x + 1, y)
def up(x, y): return (x, y + 1)
def down(x, y): return (x, y - 1)

def getCoordinate(x, y):
    if ((x, y) == (0, 0)):
        return (1, 0)
    if (abs(x) == abs(y)):
        if (y > 0):
            if (x > 0):
                return left(x, y) 
            else:
                return down(x, y)  
        else:
            return right(x, y)  
    if (x > 0 and abs(y) < x):
        return up(x, y)
    if (y > 0 and abs(x) < y):
        return left(x, y)
    if (x < 0 and abs(y) < abs(x)):
        return down(x, y)
    if (y < 0 and abs(x) < abs(y)):
        return right(x, y)
	

def getSumAdj(coordinates, matrix):
    x,y=coordinates
    value=0
    print(coordinates)
    if (x+1,y) in matrix:
        value=value+matrix[(x+1,y)]
    if (x,y-1) in matrix:
        value=value+matrix[(x,y-1)]
    if (x-1,y) in matrix:
        value=value+matrix[(x-1,y)]
    if (x,y+1) in matrix:
        value=value+matrix[(x,y+1)]
    if (x+1,y+1) in matrix:
        value=value+matrix[(x+1,y+1)]
    if (x-1,y+1) in matrix:
        value=value+matrix[(x-1,y+1)]
    if (x-1,y-1) in matrix:
        value=value+matrix[(x-1,y-1)]
    if (x+1,y-1) in matrix:
        value=value+matrix[(x+1,y-1)]

    return value
    





value=1
coordinates=(0,0)
matrix={coordinates:value}
while value<=num:
    x,y=coordinates
    coordinates=getCoordinate(x,y)
    value=getSumAdj(coordinates, matrix)
    matrix[coordinates]=value


print(matrix)
print(value)








	








	


