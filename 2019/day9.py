from intcode_class2 import Intcode
#from test import Intcode

def list_op():
    opcodes=[]
    with open('input_day9.txt') as f:
        for line in f:
            for op in line.strip().split(','):
                opcodes.append(int(op))
    return opcodes


file1 = list_op()

machine=Intcode("DAY9", file1)
machine.codeRun(1)

machine=Intcode("Part2", file1)
machine.codeRun(2)