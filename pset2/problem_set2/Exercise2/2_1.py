#Kyle Verdeyen
#Problem set 2, exercise 2, problem 1
#Computational Genomics: Data Analysis
#usage: 2_1.py trainingdat traininglab testdat testlab
import numpy as np
import sys
import itertools

#2mers, 3mers, 4mers list build
bases = ['A', 'T', 'G', 'C']
k=2
kmers2=list(itertools.product(bases, repeat=k))
k=3
kmers3=list(itertools.product(bases, repeat=k))
k=4
kmers4=list(itertools.product(bases, repeat=k))

#build lists
trainingdata = open(sys.argv[1]).readlines()
traininglabels = open(sys.argv[2]).readlines()
testdata = open(sys.argv[3]).readlines()
testlabels = open(sys.argv[4]).readlines()

