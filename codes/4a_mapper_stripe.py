#!/usr/bin/env python3

import sys

# Emit A - {B: value, C: value, ... etc.}
for line in sys.stdin:

    line = line.strip()

    line = line.split()

    for item in line:
        t = dict()
        for b in line[line.index(item)+1:]:
            if b in t: 
                t[b] += 1
            else:
                t[b] = 1
        print(item+'-'+str(t)+'\n')

