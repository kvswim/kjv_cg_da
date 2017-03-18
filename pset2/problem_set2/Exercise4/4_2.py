#Kyle Verdeyen
#Pset2, Ex4
#Computational Genomics: Data Analysis
#usage: python 4_1.py expr.txt
import numpy as np
import sys
from sklearn.cluster import KMeans

#4.1 n/a as i'm not 638

#4.2
data = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,1816))
#pred = KMeans(n_clusters=5, max_iter=10, init=data[:,:5]).fit(data)
#not sure why the above line won't work, just gives me an error that 
#my vectors don't match the number of clusters
pred = KMeans(n_clusters=5, max_iter=10).fit(data)
print(pred.cluster_centers_)
print('number of samples in each cluster:', len(pred.cluster_centers_[0]))

#4.3
# a) There are n*k free parameters. (n is # of samples) 
#The likelihood is represented by 
#sum(mean(n)-x_n)^2
# b)
for x in range(2,10):
#	pred = KMeans(n_clusters=x, max_iter=10, init=data[:,:x]).fit(data)
	pred = KMeans(n_clusters=x, max_iter=19).fit(data)
	print('k=',x)
# c) k=10
