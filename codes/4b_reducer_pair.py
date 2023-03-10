#!/usr/bin/env python

# REDUCER

# INPUT A B C: 1

# input 2 count_2item.txt -> (A,B): Count(A,B)

count3 = dict() # COUNT(A,B,C)

for line in sys.stdin:
    
    line = line.strip()
    i,v = line.split(':')
    
    if i in count3:
        count3[i] += int(v)
    else:
        count3[i] = int(v)

count2 = dict() # COUNT(A,B)

for line in sys.stdin:
    i, v = line.split('-')
    if i in count2:
        count2[i] += int(v)
    else:
        count2[i] = int(v)

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

