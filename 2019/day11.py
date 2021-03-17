
from intcode_class3 import Computer

class Painting:
    def __init__(self, input_vals, initial_color=0):
        self.computer = Computer(input_vals)
        self.direction = 0
        self.x, self.y = 0, 0
        self.painted = {(self.x, self.y): initial_color}

    def paint(self):
        while not self.computer.done:
            starting_color = self.painted[(self.x, self.y)] if (self.x, self.y) in self.painted else 0
            self.painted[(self.x, self.y)] = self.computer.calculate(starting_color)
            self.change_direction(self.computer.calculate())
            self.rotate()

    def change_direction(self, rotate_direction):
        if rotate_direction == 0:
            self.direction = (self.direction - 1) % 4
        else:
            self.direction = (self.direction + 1) % 4

    def rotate(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1        

    def show_painting(self):
        data = [[" " for _ in range(50)] for _ in range(6)]
        for x, y in self.painted.keys():
            color = self.painted[(x, y)]
            data[abs(y)][x] = " " if color == 0 else "*"
        for row in data:
            print(''.join(row))

def list_op():
    opcodes=[]
    with open('input_day11.txt') as f:
        for line in f:
            for op in line.strip().split(','):
                opcodes.append(int(op))
    return opcodes


file1 = list_op()



painting=Painting(file1)
painting.paint()
print("Part 1: "+str(len(painting.painted.keys())))

letter_painting = Painting(file1, 1)
letter_painting.paint()
print(f"Part 2: ")
letter_painting.show_painting()





"""from intcode_class3 import Computer
from intcode_class2 import Intcode
#from test import Intcode

def list_op():
    opcodes=[]
    with open('input_day11.txt') as f:
        for line in f:
            for op in line.strip().split(','):
                opcodes.append(int(op))
    return opcodes


file1 = list_op()


#machine.codeRun(0)
def paint_execute(code, initial_color):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    machine=Intcode("DAY11", code)
    x=y=direction= 0
    panel = { (x, y): initial_color }


    while machine.getCode() !=99:
        #print("X Y "+str(x)+","+str(y))
        input_value=(panel[(x, y)] if (x, y) in panel else 0)
        #input_value=0
        print("input_value "+str(input_value))
        print("PANEL "+str(panel))
        color = machine.codeRun(input_value)
        direction_new = machine.codeRun( input_value)
        print("operation_ "+str(machine.getCode()))
        print("color "+str(color))
        print("direction new "+str(direction_new))
        if machine.getCode() !=99:
            panel[(x, y)] = color
            print("PANEL "+str(panel))
            direction = ((direction + 1) if direction_new == 1 else (direction - 1 + len(directions))) % len(directions)
            x, y = x + directions[direction][0], y + directions[direction][1]
    
    return panel


def build_registration(panel_points):
    registration = [[' ']*40 for _ in range(6)]
    for row in range(6):
        for col in range(40):
            if panel_points.get((col, row), 0) == 1:
                registration[row][col] = '*'
    return '\n'.join(''.join(row) for row in registration)




part1 = len(paint_execute(file1, 0))
print("PART 1 "+str(part1))

part2 = build_registration(paint_execute(file1, 1))
print(part2)


        





"""

