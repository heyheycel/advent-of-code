class Intcode:
 
    #instance attributes:
    #intcode - the intcode in memory
    #phase - the phase of the engine
    #pointer - a memory of where the intcode pointer instruction is/was
    #inputCounter - controls the input flow of the machine
 
    def __init__(self, name, file1):
        self.name = name
        self.intcode=file1
        for i in range(10000):
            self.intcode.append(0)
   

    def codeRun(self, inputValue):
 
        code = self.intcode
 
        pos = 0
       
        relPos = 0      #set the relative position
 
        #function to return a five-element array to represent the intcode
        def intcodeArray(int1):
            intcode = list(str(int1))
            if(len(intcode)<5):
                for i in range(5-len(intcode)):
                    intcode.insert(0,"0")
            for i in range(len(intcode)):
                intcode[i] = int(intcode[i])
            return intcode
 
        ##inst[4] and inst[3] are the opcode
        ##inst[2] is the mode of the first parameter
        ##inst[1] is the mode of the second parameter
        ##inst[0] is the mode of the third parameter
 
        #function to return the value of a position, given its mode
        def value(mode, pos1):
            val = 0
            if(mode==0):        #position mode
                val = code[code[pos1]]
            elif(mode==1):      #immediate mode
                val = code[pos1]
            elif(mode==2):      #relative mode
                val = code[code[pos1]+relPos]
            return val
 
        #run the intcode
        while(code[pos]!=99):
           
            inst = intcodeArray(code[pos])
 
            #add two values
            if(inst[4]==1):
                two = pos+1
                three = pos+2
                four = pos+3
 
                if(inst[0]==0):
                    heather = code[four]
                elif(inst[0]==1):
                    heather = four
                elif(inst[0]==2):
                    heather = code[four] + relPos
 
                code[heather] = value(inst[2],two) + value(inst[1],three)
                pos += 4
 
            #multiply two values
            elif(inst[4]==2):    
                two = pos+1
                three = pos+2
                four = pos+3
 
                if(inst[0]==0):
                    heather = code[four]
                elif(inst[0]==1):
                    heather = four
                elif(inst[0]==2):
                    heather = code[four] + relPos

                print("heather "+ str(heather))
                print(relPos)
                print(len(code))
 
                code[heather] = value(inst[2],two) * value(inst[1],three)
                pos += 4
 
            #take an input value
            elif(inst[4]==3):
               
                if(inst[2]==0):
                    code[code[pos+1]] = inputValue
                elif(inst[2]==1):
                    code[pos+1] = inputValue
                elif(inst[2]==2):
                    code[code[pos+1]+relPos] = inputValue
                   
                pos += 2
 
            #return an output value
            elif(inst[4]==4):
                print("Returned " + str(value(inst[2],(pos+1))))
                pos += 2
 
            #if first parameter != 0, jump to position given by the second parameter
            elif(inst[4]==5):
               
                two = pos+1
                three = pos+2
 
                if(value(inst[2],two)!=0):
                    pos = value(inst[1],three)
                else:
                    pos += 3
 
            #if first parameter is zero, jump to position given by the second parameter
            elif(inst[4]==6):
               
                two = pos+1
                three = pos+2
 
                if(value(inst[2],two)==0):
                    pos = value(inst[1],three)
                else:
                    pos += 3
 
            #based on whether first parameter < second parameter,
            #store 1 or 0 in the position given by the third parameter
            elif(inst[4]==7):
               
                two = pos+1
                three = pos+2
                #four = code[pos+3]
                four = pos+3
 
                if(inst[0]==0):
                    heather = code[four]
                elif(inst[0]==1):
                    heather = four
                elif(inst[0]==2):
                    heather = code[four] + relPos                
 
                if(value(inst[2],two) < value(inst[1],three)):
                    code[heather] = 1
                else:
                    code[heather] = 0
                pos += 4
 
            #based on whether first parameter == second parameter,
            #store 1 or 0 in the position given by the third parameter.
            elif(inst[4]==8):
               
                two = pos+1
                three = pos+2
                #four = code[pos+3]
                four = pos+3
 
                if(inst[0]==0):
                    heather = code[four]
                elif(inst[0]==1):
                    heather = four
                elif(inst[0]==2):
                    heather = code[four] + relPos                
 
                if(value(inst[2],two) == value(inst[1],three)):
                    code[heather] = 1
                else:
                    code[heather] = 0
                pos += 4
 
            #change the relative position by the only parameter
            elif(inst[4]==9):
                relPos += value(inst[2],(pos+1))
 
                pos += 2
        