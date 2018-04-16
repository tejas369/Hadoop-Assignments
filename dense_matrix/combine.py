#!/usr/bin/env python

import sys


dict1={}
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t')
    
    
    if key in dict1:
        dict1[key].append(value)
    else:
        dict1[key]= [value]


for i in range(0,10,2):
    key = str(i)+","+str
    combine()
        
