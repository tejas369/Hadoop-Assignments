#!/usr/bin/env python
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

count = 0
currentKey = None

#### Complete the rest of the code


def printResults():
    for k in dict1.keys():
	print '%s\t%d' % (str(k),dict1[k])

dict1 = {}

for line in sys.stdin:
    line = line.strip()

    key, value = line.split('\t')
    if key not in dict1:
	dict1[key] = count + 1;
        
    else:
        dict1[key] += 1;

printResults()
