#Kyle Verdeyen
#Comuptational Genomics: Data Analysis
#Problem Set 3, Exercise 2
#kverdey1@jhu.edu
#Usage: python 2_1.py
import numpy as np
from numpy.linalg import inv

e1 = np.array([[1.0, 0.4328], [0.4328, 1.0]])
e2 = np.array([[1.0, -0.3184], [-.3184, 1.0]])
e3 = np.array([[1.0, .517], [.517, 1.0]])
print('E1:')
print(e1)
e1inv = inv(e1)
print('E-1:')
print(e1inv)
print('E2:')
print(e2)
e2inv = inv(e2)
print('E-2:')
print(e2inv)
print('E3:')
print(e3)
e3inv = inv(e3)
print('E-3:')
print(e3inv)
#2.2: The signs invert depending on the input matrix.
#A positive covariance matrix will result in a negative
#inverse covariance matrix and vice versa. This means we 
#can conclude that if the inverse covariance matrix shows
#a negative edge/correlation, the input gene pair was positive
#in its raw normalized state, and also the other way around.
#A positive normalized value and a negative edge can lead to
#lower loss in a training function. 
