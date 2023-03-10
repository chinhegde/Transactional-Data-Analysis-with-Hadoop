#!/usr/bin/env python

# REDUCER

# INPUT A - {(B,C):1, (C,D):1, ... etc.}

import sys

# COUNT(A,B)

count2 = dict() 

for line in sys.stdin:
    i, v = line.split('-')
    if i in count2:
        count2[i] += int(v)
    else:
        count2[i] = int(v)


# Input from mapper


count3 = dict()

for line in sys.stdin:
    
    line = line.strip()
    a,arr = line.split('-')
    
    arr = eval(arr)
    
    for k,v in arr.items():
        if str(a+' '+k) in count3:
            count3[a+' '+k] += 1
        else:
            count3[a+' '+k] = 1


# Prob (A|B,C) = COUNT(A,B,C)/COUNT(B,C) 

prob = dict()

for k,v in count3.items():
    
    a,b,c = k.split()
    
    if a+'|'+b+','+c not in prob:
        prob[a+'|'+b+','+c] = round(int(v)/count2[b+' '+c],4)
        prob[b+'|'+a+','+c] = round(int(v)/count2[a+' '+c],4)    
        prob[c+'|'+a+','+b] = round(int(v)/count2[a+' '+b],4)

for k,v in prob.items():
    print(k,v)

