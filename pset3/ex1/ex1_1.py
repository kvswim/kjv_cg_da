#Kyle Verdeyen
#Problem set 3, exercise 1
#Computational Genomics: Data Analysis
#usage: ex1_1.py genotype_population.csv population_info.csv

import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA

#1.1
gene_pop = np.loadtxt(sys.argv[1], delimiter=",", skiprows=1, usecols=range(1, 9027),  ndmin=2)
scale(gene_pop)

#1.2
#2a
pca = PCA(n_components=20)
pca.fit(gene_pop)
plt.figure()
X = pca.components_
forlater = X #used in 1.3
Y = np.dot(X, gene_pop.T)
plt.title('PCA 2a')
plt.plot(X,Y)
plt.show()
#2b
pca.fit_transform(gene_pop)
plt.figure()
X = pca.components_
Y = np.dot(X, gene_pop.T)
plt.title('PCA 2b')
plt.plot(X,Y)
plt.show()

#1.3
forlater = forlater.T #because we want nxk not kxn
forlater = np.dot(gene_pop,forlater)
pc1 = forlater[:,0]
pc2 = forlater[:,1]
pc3 = forlater[:,2]
pc4 = forlater[:,3]
pc8 = forlater[:,7]
pc9 = forlater[:,8]
races = np.loadtxt(sys.argv[2], ndmin=1, skiprows=1, usecols=(2,), delimiter=',', dtype='string')
races2 = [x.strip("\"") for x in races]
#PC1 vs PC2
plt.figure()
df = pd.DataFrame(dict(x=pc1, y=pc2, color=races2))
colors = {'CEU':'red', 'YRI':'blue', 'JPT':'green', 'HCB':'orange'}
plt.scatter(df['x'],df['y'], c=df['color'].apply(lambda a: colors[a]))
plt.show()
#PC2 VS PC3
plt.figure()
df = pd.DataFrame(dict(x=pc2, y=pc3, color=races2))
plt.scatter(df['x'], df['y'], c=df['color'].apply(lambda a: colors[a]))
plt.show()
#PC3 VS PC4
plt.figure()
df = pd.DataFrame(dict(x=pc3, y=pc4, color=races2))
plt.scatter(df['x'],df['y'],c=df['color'].apply(lambda a:colors[a]))
plt.show()
#PC8 VS PC9
plt.figure()
df = pd.DataFrame(dict(x=pc8, y=pc9, color=races2))
plt.scatter(df['x'],df['y'],c=df['color'].apply(lambda a:colors[a]))
plt.show()

#1.3.i
#4 different clusters
#1.3.ii
#D (pc8 vs pc9)
