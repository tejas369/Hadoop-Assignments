#!/usr/bin/env python
import sys
import numpy

### Prevents pipe IO errors for large files.
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)
###

# read parameters from distributed cache - nbins, minmeanmax
f = open('nbins','r') # read nbins file
params = f.readline().strip().split() # read nbins file
nbins = int(params[0]) # set maximum number of bins
f.close()

f = open('mmm','r') # open mmm file

'''
Read mmm file and assign min, max and mean values.
File read operation in similar to above reading procedure.
'''
params =  f.readline().strip().split()
xmax = float(params[1]) 
params = f.readline().strip().split()
xmean = float(params[1])
params = f.readline().strip().split()
xmin = float(params[1])
f.close()



dx = (xmax-xmin)/nbins # bin width calculation


# compute bin centre
#### complete this code

def bin_center(x):
	bce = xmin + (x-1) * dx + dx/2
	return bce





# process input data
#### complete this code

for line in sys.stdin:
   	line = line.strip()

	words = line.split()
    	a = float(words[0])

	for i in range (1,nbins+1):
		if a>xmin+(i-1)*dx and a <=xmin+i*dx:
			binCenter = bin_center(i)
	print '%s\t%f' % (str(binCenter),a)
