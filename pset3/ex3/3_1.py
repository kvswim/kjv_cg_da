#Kyle Verdeyen
#Problem Set 3, Exercise 3
#Computational Genomics: Data Analysis
#usage: python 3_1.py gmm.csv
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

#3.1
def myGMM(data, k, max_iter, conv_tol):
	gaussmix = GaussianMixture(n_components=k, max_iter=max_iter, reg_covar=conv_tol)
	gaussmix.fit(data)
	pi = gaussmix.weights_
	mean = gaussmix.means_
	mean=mean.T
	z = gaussmix.predict_proba(data)
	n = len(data)-1
	assign = max(z[n,:])
	return{'pi':pi, 'mean':mean, 'z':z, 'assign':assign}


#3.2
input = np.loadtxt(sys.argv[1], delimiter=',', ndmin=2, skiprows=1, usecols=range(2, 12))
gmm = myGMM(input, 3, 100, 1e-6)
print('Number of samples in each component:')
print(len(gmm['mean']))


#3.3
X = input[2]
Y = input[3]
plt.figure()
plt.plot(X, Y)
plt.show()
