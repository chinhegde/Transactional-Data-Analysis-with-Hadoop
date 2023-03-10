#!/usr/bin/env python

import sys

# item count -> gets Count(A)

items = dict()
lines = list()

for i in sys.stdin:
    
    i = i.strip()
    lines.append(i)
    i = i.split()
    
    for j in i:
        if j in items: items[j] += 1
        else: items[j] = 1

# Emit (A, B) : Count(A) Count(B)

for line in lines:
    line = line.split()

    k = [(line[i],j) for i in range(len(line)) for j in line[i+1:]]
        
    for i in k:
        print(i[0]+' '+i[1]+':'+str(items[i[0]])+' '+str(items[i[1]]))

