from sklearn import linear_model
import numpy as np

'''read first line of input file'''
col_names = []
filename=sys.argv[1]
f = open(filename)
col_names = f.readline().strip().split(',')
f.close()

'''read data from file using genfromtxt'''
data=np.genfromtxt(filename, delimiter=',', skip_header=1)
data.shape
