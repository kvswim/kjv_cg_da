#Kyle Verdeyen
#CG:DA PSET1
#Feb 2017
#Assumes necessary files are in same directory as script
from sklearn import linear_model
import numpy as np
import sys

#read & form second column of genotype  file
genotype = np.genfromtxt('genotype.csv', delimiter=',', skip_header=1, usecols=(range(1,9089)))
genotype.shape
temp = 0
for x in range(0,len(genotype)):
	counter = 0
	for y in range(0,279):
		if(genotype[x,y] == 1 or genotype[x,y]==2):
			++counter
	if(counter/558>.1):
		++temp
print(temp)
