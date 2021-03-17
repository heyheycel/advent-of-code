class Intcode:
 
    #instance attributes:
    #intcode - the intcode in memory
    #phase - the phase of the engine
    #pointer - a memory of where the intcode pointer instruction is/was
    #inputCounter - controls the input flow of the machine
 
    def __init__(self, name, file1, phase, pointer):
        self.name = name
        self.phase = phase
        self.pointer = pointer
        self.intcode=file1
        self.inputCount=0
   
    def getCode(self):
        return self.intcode[self.pointer]


    def codeRun(self, inputValue):
        def intcodeArray(int1):
            ##inst[4] and inst[3] are the opcode
            #inst[2] is the mode of the first parameter
            ##inst[1] is the mode of the second parameter
            ##inst[0] is the mode of the third parameter
            intcode = list(str(int1))
            if(len(intcode)<5):
                for i in range(5-len(intcode)):
                    intcode.insert(0,"0")
            for i in range(len(intcode)):
                intcode[i] = int(intcode[i])
            return intcode
        def value(mode, pos1, code):
            #function to return the value of a position, given its mode
            val = 0
            if(mode==0):
                val = code[code[pos1]]
            elif (mode==1):
                val = code[pos1]
            return val
 
        opcodes = self.intcode
        pointer = self.pointer
        #print(self.name + " starting at position " + str(pos))
 
        
 
        if(opcodes[pointer] == 99):
            #print(self.name + " stopped at " + str(pos) + ", with code " + str(code[pos]))
            returnValue = None
 
        #run the intcode
        while(opcodes[pointer]!=99):
            inst = intcodeArray(opcodes[pointer])
 
            #add two values
            if(inst[4]==1):
                x = pointer+1
                y = pointer+2
                z = opcodes[pointer+3]
               
                opcodes[z] = value(inst[2],x, opcodes) + value(inst[1],y, opcodes)
                pointer += 4
 
            #multiply two values
            elif(inst[4]==2):    
                x = pointer+1
                y = pointer+2
                z = opcodes[pointer+3]
 
                opcodes[z] = value(inst[2],x,opcodes) * value(inst[1],y, opcodes)
                pointer += 4
 
            #take an input value
            elif(inst[4]==3):
               
                if(self.inputCount == 0):
                    choice = self.phase
                    self.inputCount += 1
                else:
                    choice = inputValue
               
                if(inst[2]==0):
                    opcodes[opcodes[pointer+1]] = choice
                else:
                    opcodes[pointer+1] = choice
                   
                pointer += 2
 
            #return an output value
            elif(inst[4]==4):
                returnValue = value(inst[2],(pointer+1),opcodes)
                #print(self.name + " stopped at " + str(pos) + ", with code " + str(code[pos]))
                pointer += 2
                self.pointer = pointer
                break
 
            #if first parameter != 0, jump to position given by the second parameter
            elif(inst[4]==5):
               
                x = pointer+1
                y = pointer+2
               
                if(value(inst[2],y, opcodes)!=0):
                    pointer = value(inst[1],y,opcodes)
                else:
                    pointer += 3
 
            #if first parameter is zero, jump to position given by the second parameter
            elif(inst[4]==6):
               
                x = pointer+1
                y = pointer+2
               
                if(value(inst[2],x)==0):
                    pointer = value(inst[1],y)
                else:
                    pointer += 3
 
            #based on whether first parameter < second parameter,
            #store 1 or 0 in the position given by the third parameter
            elif(inst[4]==7):
               
                x = pos+1
                y = pos+2
                z = code[pos+3]
               
                if(value(inst[2],x,opcodes) < value(inst[1],y,opcodes)):
                    opcodes[z] = 1
                else:
                    opcodes[z] = 0
                pointer += 4
 
            #based on whether first parameter == second parameter,
            #store 1 or 1 in the position given by the third parameter.
            elif(inst[4]==8):
               
                x= pos+1
                y = pos+2
                z = code[pos+3]
               
                if(value(inst[2],x,opcodes) == value(inst[1],y,opcodes)):
                    opcodes[z] = 1
                else:
                    opcodes[z] = 0
                pointer += 4
 
        return returnValue