from random import *

f = open('input/part-00000', 'w')

for i in range (0, 10):
	for j in range (0, 10):
		f.write("A "+ str(i) + " " + str(j) + " " + str(randint(1,11)) + "\n")

for i in range (0, 10):
	for j in range (0, 10):
		f.write("B "+ str(i) + " " + str(j) + " " + str(randint(1,11)) + "\n")

f.close()

