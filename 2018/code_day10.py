from re import findall
from collections import defaultdict


class Coordinate():
    def __init__(self, x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    def step(self):
        self.x += self.vx
        self.y += self.vy
 
data=[]
for line in open('input_day10.txt').readlines():
    numbers=findall(r'-?\d+', line)
    x,y,vx,vy=numbers
    coordinate=Coordinate(int(x), int(y), int(vx), int(vy))
    data.append(coordinate)


#print(data)


def pprint(points):
    min_x = min(p.x for p in points)
    min_y = min(p.y for p in points)

    img = [[0 for i in range(10)] for i in range(100)]
    for p in points:
        img[p.x - min_x][p.y - min_y] = 1
    result = ""
    for i in range(10):
        for j in range(100):
            if img[j][i]==1:
                result += "#"
            else:
                result += "."
        result += "\n"
    return result

count=0
while True:
    y = []
    for point in data:
        point.step()
        y.append(point.y)

    count+=1    
    if max(y) - min(y) <= 12:
        print("Seconds: "+str(count))
        print(pprint(data))
        break

    

    







        