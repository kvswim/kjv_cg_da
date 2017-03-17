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
trainingdata = open(sys.argv[1]).readlines() #data is 1-2176
traininglabels = open(sys.argv[2]).readlines()
testdata = open(sys.argv[3]).readlines() #1-1001
testlabels = open(sys.argv[4]).readlines()

print(kmer(trainingdata, 2)
#test = CountVectorizer(vocabulary=kmers2)
#X = test.fit_transform("".join(trainingdata)).toarray()
#print(X)

def kmer(data, k):
	dict = {}
	for x in range(1, len(data)):
		temp = data[x]
		for y in range(len(temp)+1-k):
			kmer = dna[y:y+k]
			dict[kmer]=dict.get(kmer, 0) + 1
	return dict
