#!/usr/bin/env python3

import itertools

for line in sys.stdin:
    
    line = line.strip()
    line = line.split()

    for i,j,k in itertools.combinations(line, 3):
        print(i+' '+j+' '+k+": 1\n")

