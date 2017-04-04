#Kyle Verdeyen
#Problem set 3, exercise 1
#Computational Genomics: Data Analysis
#usage: ex1_1.py genotype_population.csv

import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

#problem 1
gene_pop = np.loadtxt(sys.argv[1], delimiter=",", skiprows=1, usecols=range(1, 9026),  ndmin=2)
scale(gene_pop)

#problem 2
#2a
pca = PCA(n_components=20)
pca.fit(gene_pop)
plt.figure()
X = pca.components_
Y = np.dot(X, gene_pop.T)
plt.title('PCA 2a')
plt.show()
#2b
pca.fit_transform(gene_pop)
plt.figure()
X = pca.components_
Y = np.dot(X, gene_pop.T)
plt.title('PCA 2b')
plt.show()

