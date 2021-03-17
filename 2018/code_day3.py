from collections import defaultdict

with open("input_day3.txt", "r") as arch:
	input = arch.read().strip().split('\n')



def parse_claim(s):
    identifier, arroba, dist, size = s.split(' ')
    fromleft, fromtop = map(int, dist[:-1].split(','))
    width, height = map(int, size.split('x'))
    return identifier, fromleft, fromtop, width, height



#part 1
rect = defaultdict(int)
for claim in input:
	iden, leftoff, topoff, w, h = parse_claim(claim)
	for dx in range(w):
         for dy in range(h):
             rect[(leftoff+dx, topoff+dy)] += 1

count = 0
for (r,c),v in rect.items():
	if v >= 2:
		count += 1

print (count)


#part 2:
for claim in input:
	iden, leftoff, topoff, w, h = parse_claim(claim)
	possible=True
	for dx in range(w):
		for dy in range(h):
			if rect[(leftoff+dx, topoff+dy)]>1:
				possible=False
	if (possible==True):
		print(iden)
