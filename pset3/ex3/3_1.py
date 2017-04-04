#usage: python 3_1.py gmm.csv
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

def myGMM(data, k, max_iter, conv_tol):
	gaussmix = GaussianMixture(n_components=k, max_iter=max_iter, reg_covar=conv_tol).fit(data)
	pi = gaussmix.weights_
	mean = gaussmix.means_
	z = gaussmix.score_samples
	print(type(z))
#assign = max(z[len(data),:])

input = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(2,11), ndmin=2, delimiter=',')
gmm = myGMM(input, 3, 100, 1e-6)
