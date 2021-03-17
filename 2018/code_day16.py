s = open('input_day16.txt',"r").read()
part1, part2 = s.split("\n\n\n")

blocks = part1.split("\n\n")
#print(blocks)






class Resolution:
	def __init__(self):
		self.registers=[0]*4
		self.opcodes={
		'addr':self.addr,
		'addi':self.addi,
		'mulr':self.mulr,
		'muli':self.muli,
		'banr':self.banr,
		'bani':self.bani,
		'borr':self.borr,
		'bori':self.bori,
		'setr':self.setr,
		'seti':self.seti,
		'gtir':self.gtir,
		'gtri':self.gtri,
		'gtrr':self.gtrr,
		'eqir':self.eqir,
		'eqri':self.eqri,
		'eqrr':self.eqrr
		}


	def set_registers(self,values):
		for i in range(len(values)):
			self.registers[i]=values[i]

	#16 possible opcodes by function
	def addr(self,a,b,c):
		self.registers[c]=self.registers[a]+self.registers[b]

	def addi(self,a,b,c):
		self.registers[c]=self.registers[a]+b

	def mulr(self,a,b,c):
		self.registers[c]=self.registers[a]*self.registers[b]

	def muli(self,a,b,c):
		self.registers[c]=self.registers[a]*b
	
	def banr(self,a,b,c):
		self.registers[c]=self.registers[a] & self.registers[b]

	def bani(self,a,b,c):
		self.registers[c]=self.registers[a] & b

	def borr(self,a,b,c):
		self.registers[c]=self.registers[a] | self.registers[b]

	def bori(self,a,b,c):
		self.registers[c]=self.registers[a] | b

	def setr(self,a,b,c):
		self.registers[c]=self.registers[a]

	def seti(self,a,b,c):
		self.registers[c]= a


	def gtir(self,a,b,c):
		self.registers[c]= int(a>self.registers[b])

	def gtri(self,a,b,c):
		self.registers[c] = int(self.registers[a] > b)

	def gtrr(self, a, b, c):
		self.registers[c] = int(self.registers[a] > self.registers[b])

	def eqir(self, a, b, c):
		self.registers[c] = int(a == self.registers[b])

	def eqri(self, a, b, c):
		self.registers[c] = int(self.registers[a] == b)

	def eqrr(self, a, b, c):
		self.registers[c] = int(self.registers[a] == self.registers[b])

	def possible_opcodes(self,before,instruction,after):
		result=set()
		for name,opcode in self.opcodes.items():
			self.set_registers(before)
			opcode(*instruction[1:])
			if self.registers==after:
				result.add(name)
		return result






result=0
resolution=Resolution()
for block in blocks:
	before,instruction,after=block.splitlines()
	before=[int(n) for n in before[9:-1].split(", ")]
	#print(before)
	instruction=[int(n) for n in instruction.split()]
	#print(instruction)
	after=[int(n) for n in after[9:-1].split(", ")]
	#print(after)
	possible_opcodes=resolution.possible_opcodes(before,instruction,after)

	if len(possible_opcodes) >=3:
		result+=1



print("Result: "+str(result))













































