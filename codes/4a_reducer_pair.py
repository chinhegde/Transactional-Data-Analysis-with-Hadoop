#!/usr/bin/env python

import sys

# input -> (a,b): count(a), count(b)

count = dict() # COUNT(A, B)
ind = dict() # COUNT(A)

for line in sys.stdin:
    line = line.strip()
    line = line.split(':')

    if line[0] in count: count[line[0]] += 1
    else: count[line[0]] = 1

    a, b = line[0].split()
    ac, bc = list(map(int,line[1].split()))

    if a not in ind:
        ind[a] = ac
    if b not in ind: 
        ind[b] = bc


cprob = dict() # conditional probability

for iset in count:
    a, b = iset.split()
    
    # P(A|B) = COUNT(A,B)/COUNT(B)
    
    if a+'|'+b not in cprob or b+'|'+a not in cprob:
        cprob[a+'|'+b] = round(count[iset]/ind[b],4)
        cprob[b+'|'+a] = round(count[iset]/ind[a],4)

for k,v in cprob.items():
    print(k,v)

