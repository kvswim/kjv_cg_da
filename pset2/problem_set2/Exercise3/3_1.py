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
from scipy.stats import pearsonr
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
print('3.3 disabled with Agg for ugrad, see code')
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
covs = np.loadtxt(sys.argv[2], skiprows=1, usecols=range(1, 74))
X = pca.components_
count = 0
print('#3.4:')
#hard coded indices because i'm a heathen
for i in range(0,10):
	for j in range(0,3):
		pearson = pearsonr(X[i], covs[j])
		print(pearson)
		if(abs(pearson[0])>0.2 and pearson[1] < 0.05):
			count=count+1 
print('Strongly correlated PC count:', count)

#3.5
phen = np.genfromtxt(sys.argv[3], delimiter='\t',  skip_header=1, usecols =(1))
print('#3.5:')
for x in range(0,len(phen)):
	for j in range(0,3):
		pearson = pearsonr(phen, covs[j])
		print(pearson)

#I don't think data is confounded as the numbe of significant genes
#is similar to what we found in 3.4

#3.6
