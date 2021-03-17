
from collections import defaultdict 
  

with open("input_day7.txt", "r") as arch:
	data = arch.read().strip().split('\n')



class Graph:
    def __init__(self, base_time, num_workers):
        #adjacent vertices
        self.dependencies=[]
        self.graph = {}
        self.base_time=base_time
        self.num_workers=num_workers
    def addDependencies(self,u,v):
        self.dependencies.append((u,v))
    def reverseEdges(self): 
        for before, after in self.dependencies:
            if before not in self.graph:
                self.graph[before] = []
            if after not in self.graph:
                self.graph[after] = []
            self.graph[after].append(before)
    def travelGraph(self):
        self.reverseEdges()
        self.graph=sorted(self.graph.items(),key=lambda t: t[0])
        path=[]

        while len(path) !=len(self.graph):
            for after, before in self.graph:
                if after not in path and all(edge in path for edge in before):
                    path.append(after)
                    break
        print("Path part 1")
        print(path)
        print("".join(path))
    def travel_time(self):
        alphabet={'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        path=[]
        current_stack={}
        time=0

        while len(path) !=len(self.graph):
            for after, before in self.graph:
                if after not in path and after not in current_stack and all(edge in path for edge in before):
                    current_stack[after]=self.base_time+alphabet[after]
                    if len(current_stack)==self.num_workers:
                        break
            next_edge=min(current_stack.values())
            time+=next_edge
            for edge in current_stack:
                current_stack[edge]-=next_edge
                if current_stack[edge]==0:
                    path.append(edge)
            for edge in path:
                if edge in current_stack:
                    del current_stack[edge]


        print("Time: ")
        print(time)



base_time=60
num_workers=5
g=Graph(base_time,num_workers)
visited={}
for line in data:
    u=line.split()[1]
    v=line.split()[7]
    g.addDependencies(u,v)


g.travelGraph()
g.travel_time()


