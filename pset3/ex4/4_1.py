#usage: python 4_1.py expr_ceph_utah_1000.txt
import numpy as np
import sys
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.covariance import GraphLasso
from scipy.stats import pearsonr

#4.1
data = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,1001), ndmin=2)
pearson_data = (pearsonr(data[0],data[0,:]))
pearson_data = pearson_data+(pearsonr(data[1],data[1,:]))
pearson_data = pearson_data+(pearsonr(data[2],data[2,:]))
pearson_data = pearson_data+(pearsonr(data[3], data[3,:]))
pearson_data = pearson_data+(pearsonr(data[4],data[4,:]))
print(pearson_data)
#Cannot complete 2/3 of this part as 2-tail p-values are only 1 or 0. 
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
#a: glasso: 100 edges, wgcna has less
#b: all edges in wgcna are in glasso.
#c: ???
