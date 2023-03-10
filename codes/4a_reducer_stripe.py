import sys


# REDUCER

count = dict()
lines = list()

for i in sys.stdin:
    
    i = i.strip()
    line.append(i)
    a, arr = i.split('-')
    
    arr = eval(arr)
    
    for k,v in arr.items():
        if str(a+' '+k) in count:
            count[a+' '+k] += 1
        else:
            count[a+' '+k] = 1

# INPUT A - {B: value, C: value, ... etc.}

items = dict()

for i in lines:
    i = i.split()
    for j in i:
        if j in items: items[j] += 1
        else: items[j] = 1

cprob = dict() # conditional probability

for iset in count:
    a, b = iset.split()
    
    # P(A|B) = COUNT(A,B)/COUNT(B)
    
    if a+'|'+b not in cprob:
        cprob[a+'|'+b] = round(count[iset]/items[b],4)
    if b+'|'+a not in cprob:
        cprob[b+'|'+a] = round(count[iset]/items[a],4)

for k,v in cprob.items():
    print(k,v)

