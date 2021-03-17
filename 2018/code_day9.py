players=459
last_marble=71790
class Node: 
    def __init__(self, data,prev=None, next=None): 
        self.data = data 
        self.next = next
        self.prev = prev
    def node_after23(self,current_node):
        return current_node.prev.prev.prev.prev.prev.prev.prev
 




n0 = Node(0)
n0.prev = n0
n0.next = n0

current_node = n0


scores={key:0 for key in range(1,players+1)}
for turn in range(1,last_marble+1):

    if turn%23==0:
        player=(turn %players)+1
        current_node=current_node.prev.prev.prev.prev.prev.prev.prev
        scores[player]=scores[player]+turn+current_node.data
        current_node.prev.next=current_node.next
        current_node=current_node.next
    else:
        new=Node(turn,current_node.next,current_node.next.next)
        current_node.next.next.prev=new
        current_node.next.next=new
        current_node=new


print(max(scores.values()))
    




#https://github.com/badouralix/advent-of-code-2018/blob/master/day-09/part-2/jon.py





