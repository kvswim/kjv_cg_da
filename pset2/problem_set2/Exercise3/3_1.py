#Kyle Verdeyen
#Problem set 2, exercise 3, problem 1
#Computational Genomics: Data Analysis
#usage: python 3_1.py counts.txt cov.txt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
from sklearn.decomposition import PCA

#load counts.txt, perform transforms and transpose
counts = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(1,74), ndmin=2)
#first transform
for (x, y), value in np.ndenumerate(counts):
	counts[x, y] = np.log2(value+1)
means = counts.mean(axis=1)
stdevs = counts.std(axis=1)
#second
for (x,y), value in np.ndenumerate(counts):
	counts[x, y] = (value-means[x])/stdevs[y]
#transpose
counts.T

#principal component analysis, 10 components
pca = PCA(n_components = 10)
pca.fit(counts)
print("#3.2:")
print('Components:')
print(pca.components_)
print('Variance')
print(pca.explained_variance_ratio_)

#3.3
plt.figure()
pca = PCA(n_components = 2)
pca.fit(counts)
X = pca.components_
Y = np.dot(X, counts.T)
plt.title('PCA')
plt.show()

#3.4
pca = PCA(n_components = 10)
pca.fit(counts)
covs = np.loadtxt(sys.argv[2], skiprows=1, usecols=range(1, 73))
X = pca.components_
print(len(X))
