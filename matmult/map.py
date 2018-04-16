#!/usr/bin/env python

import sys



for line in sys.stdin:
    line = line.strip()

    words = line.split()
    matrix =words[0]
    row = int(words[1])
    col = int(words[2])
    value = line

    if matrix == 'A':
        for i in range (0,100):
	    key = str(row)+","+str(i)
	    print '%s\t%s' % (key,value)
    
    if matrix == 'B':
        for i in range(0,100):
            key = str(i)+","+str(col)
            print '%s\t%s' % (key,value)

    
    
