from intcode_class3 import Computer
import os


def list_op():
    opcodes=[]
    with open('input_day13.txt') as f:
        for line in f:
            for op in line.strip().split(','):
                opcodes.append(int(op))
    return opcodes


file1 = list_op()


def part1(code):
    program = Computer(code)
    blocks = 0
    game={}
    while not program.done:
        x=program.calculate()
        #print(x)
        y=program.calculate()
        #print(y)
        blocktype = program.calculate()
        #print(blocktype)
        #if tile is==2 then add 1 to number of blocks
        blocks += blocktype == 2
        game[(x, y)] = blocktype
        #print("blocks "+str(blocks))
    return blocks, game



def print_board(game):
    data = [[" " for _ in range(50)] for _ in range(20)]
    for x, y in game.keys():
        tile = game[(x, y)]
        if tile==0:
            draw="  "
        elif tile==1:
            #wall
            draw="||"
        elif tile ==2:
            draw="++"
        elif tile==3:
            draw="====="
        elif tile==4:
            draw="O"

        data[abs(y)][x] = draw
    
    for row in data:
        print(''.join(row))



blocks, game=part1(file1)
#print (game)
print_board(game)
#print(max(game.keys()))
print("Number of blocks: "+str(blocks))



#part 2


file2 = list_op()
file2[0]=2

def draw(board):
    #print(board)
    width = max(k[0] for k in board)+1
    height = max(k[1] for k in board)
    s = ''
    for row in range(height):
        for col in range(width):
            s += str(board[col, row])
        s += '\n'
    print(s)


def move_joystick(paddle, ball, program):
    input_data=0
    program.set_input_data(input_data)
    if paddle[0] < ball[0]:
        input_data = 1
        program.set_input_data(input_data)
    elif paddle[0] > ball[0]:
        input_data = -1
        program.set_input_data(input_data)
    elif paddle[0] == ball[0]:
        input_data = 0
        program.set_input_data(input_data)




def score(data):
    computer = Computer(data)
    score = 0
    ball = (0, 0)
    paddle = (0, 0)
    game={}
    tileset={0: ' ',1: '#',2: 'X',3: '-',4: 'o'}
    while not computer.done:
        update=0
        move_joystick(paddle, ball, computer)
        x = computer.calculate(0)
        y = computer.calculate()
        tile_id = computer.calculate()
        if x == -1 and y == 0:
            score = tile_id
        else:
            if tile_id in tileset:
                game[(x, y)] = tileset[tile_id]
            if tile_id == 4:
                update=1
                ball = (x, y)
            elif tile_id == 3:
                update=1
                paddle = (x, y)
        if update==1:
            os.system("cls")
            draw(game)



    return score, game

score, game = score(file2)
print("Final score: "+str(score))


