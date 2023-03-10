#!/usr/bin/env python3

import itertools
import sys

# Emit A, {(B,C):1, (B,D):1,... }

for line in sys.stdin:
    
    line = line.strip()
    line = line.split()

    # print A and combinations of line[line.index(A)+1:]
    for i in line:
        t = dict()

        for j,k in itertools.combinations(line[line.index(i)+1:], 2):
            if j+' '+k in t:
                t[j+' '+k] += 1
            else:
                t[j+' '+k] = 1
        print(i+'-'+str(t))

