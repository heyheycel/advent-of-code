class Intcode:
 
    #instance attributes:
    #intcode - the intcode in memory
    #phase - the phase of the engine
    #pointer - a memory of where the intcode pointer instruction is/was
    #inputCounter - controls the input flow of the machine
 
    def __init__(self, name, file1):
        self.name = name
        #self.intcode=file1
        self.pointer=0
        self.memory={ i : file1[i] for i in range(0, len(file1) ) }
        self.intcode=file1[:] + [0] * 3000

    def getCode(self):
        return self.intcode[self.pointer]

    def codeRun(self, inputValueD):
        opcodes = self.intcode
        pointer=self.pointer
        #print(self.name + " starting at position " + str(pointer))
        basepos=0
        memory=self.memory
        inputValue=inputValueD

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
        def value(mode, pos1):

            #function to return the value of a position, given its mode
            val = 0
            vald=0
            if(mode==0):
                val = opcodes[opcodes[pos1]]
                if memory[pos1] in memory:
                    vald=memory[memory[pos1]]
                else:
                    vald=0
            elif (mode==1):
                val = opcodes[pos1]
                if pos1 in memory:
                    vald= memory[pos1]
                else:
                    vald=0
            elif (mode==2):
                val=opcodes[opcodes[pos1]+basepos]
                if memory[pos1]+basepos in memory:
                    vald= memory[memory[pos1]+basepos]
                else:
                    vald=0
            print("val "+ str(val))
            print("vald"+ str(val))
            return val
 
       

        print("OPERATION BEFORE: "+str(memory[pointer]))
        if(opcodes[pointer] == 99):
            #print(self.name + " stopped at " + str(pointer) + ", with code " + str(opcodes[pointer]))
            returnValue = None

        #run the intcode
        while(opcodes[pointer]!=99):
            print("OPERATION AFTER: "+str(memory[pointer]))

            inst = intcodeArray(opcodes[pointer])
            instd= intcodeArray(memory[pointer])
            print("INSTRUCTION: "+str(inst[4]))
            print("INSTRUCTION D: "+str(instd[4]))
            #print(memory)

 
            #add two values
            if(inst[4]==1):
                x = pointer+1
                y = pointer+2
                z = pointer+3
                
                if (inst[0]==0):
                    heather=opcodes[z]
                    if z in memory:
                        header= memory[z]
                    else:
                        header=0
                elif(inst[0]==1):
                    heather=z
                    header=z
                elif(inst[0]==2):
                    heather= opcodes[z]+basepos
                    if z in memory:
                        header= memory[z]+basepos
                    else:
                        header=0+basepos
                print("heather "+str(heather))
                print("header" +str(header))
                
                opcodes[heather] = value(inst[2],x) + value(inst[1],y)
                memory[header]= value(instd[2],x) + value(instd[1],y)
                #print(opcodes)
                #print("memory")
                #print(memory)
                pointer += 4
 
            #multiply two values
            elif(inst[4]==2):    
                x = pointer+1
                y = pointer+2
                z = pointer+3
                
                if (inst[0]==0):
                    heather=opcodes[z]
                    if z in memory:
                        header= memory[z]
                    else:
                        header=0
                elif(inst[0]==1):
                    heather=z
                    header=z
                elif(inst[0]==2):
                    heather= opcodes[z]+basepos
                    if z in memory:
                        header= memory[z]+basepos
                    else:
                        header=basepos
                print("heather "+str(heather))
                print("header" +str(header))
                
                opcodes[heather] = value(inst[2],x) * value(inst[1],y)
                memory[header] = value(instd[2],x) * value(instd[1],y)
                #print(opcodes)
                #print("memory")
                #print(memory)
                pointer += 4
 
            #take an input value
            elif(inst[4]==3):

                if(inst[2]==0):
                    opcodes[opcodes[pointer+1]] = inputValue
                    if pointer+1 in memory:
                        if memory[pointer+1] in memory:
                            memory[memory[pointer+1]]=inputValueD
                        else:
                            inputValueD=0
                    else:
                        inputValueD=0

                elif(inst[2]==1):
                    opcodes[pointer+1] = inputValue
                    if pointer+1 in memory:
                        memory[pointer+1]=inputValueD
                    else:
                        inputValueD=0
                elif(inst[2]==2):
                    opcodes[opcodes[pointer+1]+basepos] = inputValue
                    if pointer+1 in memory:
                        if memory[pointer+1]+basepos in memory:
                            memory[memory[pointer+1]+basepos]=inputValueD
                        else:
                            inputValueD=0
                    else:
                        inputValueD=0




                print("inputValue: "+str(inputValue))  
                print("inputValueD: "+str(inputValueD))
                pointer += 2
 
            #return an output value
            elif(inst[4]==4):
                print("Value returned " + str(value(inst[2],(pointer+1))))
                returnValue = value(inst[2],(pointer+1))
                pointer += 2
                self.pointer = pointer
                #print("OPERATION EDN "+str(opcodes[pointer]))
                break
 
            #if first parameter != 0, jump to position given by the second parameter
            elif(inst[4]==5):
               
                x = pointer+1
                y = pointer+2
               
                if(value(inst[2],x)!=0):
                    pointer = value(inst[1],y)
                else:
                    pointer += 3

                self.pointer=pointer
 
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
               
                x = pointer+1
                y = pointer+2
                z = pointer+3

                if (inst[0]==0):
                    heather=opcodes[z]
                    if z in memory:
                        header= memory[z]
                    else:
                        header=0
                elif(inst[0]==1):
                    heather=z
                    header=z
                elif(inst[0]==2):
                    heather= opcodes[z]+basepos
                    if z in memory:
                        header= memory[z]+basepos
                    else:
                        header=basepos

                print("heather: "+str(heather))
                print("header: "+str(header))
               
                if(value(inst[2],x) < value(inst[1],y)):
                    opcodes[heather] = 1
                    memory[header]=1
                else:
                    opcodes[heather] = 0
                    memory[header]=0
                
                pointer += 4
 
            #based on whether first parameter == second parameter,
            #store 1 or 1 in the position given by the third parameter.
            elif(inst[4]==8):
               
                x= pointer+1
                y = pointer+2
                z = pointer+3

                if (inst[0]==0):
                    heather=opcodes[z]
                    if z in memory:
                        header= memory[z]
                    else:
                        header=0
                elif(inst[0]==1):
                    heather=z
                    header=z
                elif(inst[0]==2):
                    heather= opcodes[z]+basepos
                    if z in memory:
                        header= memory[z]+basepos
                    else:
                        header=basepos

                print("heather: "+str(heather))
                print("header: "+str(header))
               
                if(value(inst[2],x) == value(inst[1],y)):
                    opcodes[heather] = 1
                    memory[header]=1
                else:
                    opcodes[heather] = 0
                    memory[header]=0
                pointer += 4

            elif(inst[4]==9):
                basepos+=value(inst[2], (pointer+1))

                pointer+=2


        if(opcodes[pointer] == 99):
            print(self.name + " stopped at " + str(pointer) + ", with code " + str(memory[pointer]))
            returnValue = None

        return returnValue

        
        