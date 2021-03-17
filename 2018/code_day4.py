from collections import defaultdict
history = []
with open("input_day4.txt", "r") as f:
	 for line in f:
	 	history.append(line.strip())


list_in_order=sorted(history)

#print(list_in_order)

def parse_time(line):
	words=line.split()
	date=words[0][1:]
	time=words[1][:-1]
	hour=int(time.split(':')[0])
	minute=int(time.split(':')[1])
	return minute


times=defaultdict(int)
guardias=defaultdict(int)
for line in list_in_order:
	time=parse_time(line)
	if 'begins shift' in line:
		guardia=int(line.split()[3][1:])
		asleep=None
	if 'asleep' in line:
		asleep=time
	if 'wakes up' in line:
		for minute in range(asleep,time):
			times[(guardia,minute)]+=1
			guardias[guardia]+=1

#print(times)


def getMax(history, guardia):
	best=None
	for key,value in history.items():
		if best==None or value>history[best] and guardia in key:
			best=key
	return best

def getBest(history):
	best=None
	for key,value in history.items():
		if best==None or value>history[best]:
			best=key
	return best

def maxGuardia(guardias):
	v=list(guardias.values())
	k=list(guardias.keys())
	return k[v.index(max(v))]

for key,v in times.items():
	if times[key]>=15:
		print(key)


max_guardia=maxGuardia(guardias)
guardia, minute=getMax(times, max_guardia)
print(minute)
print(guardia)
print(guardia*minute)


#part 2
guardia, minute=getBest(times)
print(guardia*minute)
