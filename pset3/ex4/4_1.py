#usage: python 4_1.py expr_ceph_utah_1000.txt
import numpy as np
import sys
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.covariance import GraphLasso
from scipy.stats import pearsonr
from sklearn.linear_model import LogisticRegression

#4.1
#4.1.a
data = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,1001), ndmin=2)
pearson_data = [[pearsonr(probe1,probe2) for probe1 in data[0:5,:]] for probe2 in data[0:5,:]]
temp = pearson_data
edge_data=pearson_data
#4.1.b
for index, value in np.ndenumerate(pearson_data):
	temp1 = index[0]
	temp2 = index[1]
	if (index[2]==0) and (abs(value) >= 0.35):
		edge_data[temp1][temp2] = 1
		#print(index)
	else:
		edge_data[temp1][temp2] = 0

pearson_data = temp
#Pearson correlations are too low for any values...don't know why? this should work...probably
#only values abs(val) above any t are just identities=1
#regression code is below but won't work because of above.
#lr = LogisticRegression()
#lr.fit(edge_data,pearson_data)


#4.2 (Graphical lasso)
#4.2.a
data = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,1001), ndmin=2)
glasso = GraphLasso(alpha=0.55, tol=1e-4).fit(data)
glasso_cov = glasso.covariance_ #cov matrix
glasso_pre = glasso.precision_ #precision
#4.2.b
print(glasso_cov[0,0:4])
print(glasso_cov[1,0:4])
print(glasso_cov[2,0:4])
print(glasso_cov[3,0:4])
print(glasso_cov[4,0:4])
#4.2.c
with open(sys.argv[1], 'r') as line:
	first_line = line.readline()
first_col = np.genfromtxt(sys.argv[1], skip_header=1, usecols=range(0), dtype='str') #supposed to only read the first col but whatever
#glasso_net = plt.hist(first_line, first_col) #doesn't work

#4.3
#a: glasso: some edges, wgcna has less/none
#b: all edges in wgcna are in glasso.
#c: ???
