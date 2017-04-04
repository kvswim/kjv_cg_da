#usage: python 3_1.py gmm.csv
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

def myGMM(data, k, max_iter, conv_tol):
	n = range(data)
	d = range(data[0])
	

input = np.loadtxt(sys.argv[1], skiprows=1, usecols=range(2,11), ndmin=2)
#gmm = myGMM(input, 3, 100, 1e-6)
