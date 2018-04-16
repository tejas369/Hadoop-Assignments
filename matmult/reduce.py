#!/usr/bin/env python

import sys

 

def reduce1(key, value_list):
    A={}
    B={}
    for i in range(0,100):    
        if i not in A.keys():  
            A[i]=0  
        if i not in B.keys():  
            B[i]=0

    for x in value_list:
        para = x.split()
        if para[0]=="A":
            col = int(para[2])
            A[col]=int(para[3])
        else:
            row = int(para[1])
            B[row]=int(para[3])

    total = 0;
    for i in range(0,100):
        val = A[i] * B[i]
        total += val
    if total !=0:
        print '%s\t%d' % (key,total)



dict1={}
for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t')
    
    
    if key in dict1:
        dict1[key].append(value)
    else:
        dict1[key]= [value]

for key in dict1:
    reduce1(key, dict1[key])
    
        
    

