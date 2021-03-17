
import pdb

data = list(map(int, open('input_day8.txt').read().split()))



def sumValues(metas,values):
    total=0
    print(metas)
    print(values)
    for i in metas:
        print(i-1)
        if (i-1)>=0 and (i-1)<len(values):
            total+=values[i-1]
    return total

#print(sumValues([1,3,2,2,2],[45]))



def travel(data):
    #pdb.set_trace()
    children=data[0]
    metas=data[1]
    data=data[2:]
    meta_total=0
    values=[]
    #print(children)
    #print(metas)
    #print(data)
   

    for i in range(children):
        total, value, data=travel(data)
        meta_total+=total
        values.append(value)
        #print("Meta_total "+str(meta_total))
        #print("Value: "+str(values))

    meta_total += sum(data[:metas])
    if children==0:
        return (meta_total,sum(data[:metas]),data[metas:])
    else:

        return (meta_total,sumValues(data[:metas],values) ,data[metas:])



total, value, result=travel(data)


print("Total: "+str(total))
print("Value: "+str(value))





















"""def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals, sum(data[:metas]), data[metas:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:metas] if k > 0 and k <= len(scores)),
            data[metas:]
        )

total, value, remaining = parse(data)

print('part 1:', total)
print('part 2:', value)"""