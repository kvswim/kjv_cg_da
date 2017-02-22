from sklearn import linear_model
import numpy as np
import sys

'''read first line of input file'''
col_names = []
filename=sys.argv[1]
f = open(filename)
col_names = f.readline().strip().split(',')
f.close()

'''read data from file using genfromtxt'''
data=np.genfromtxt(filename, delimiter=',', skip_header=1)
data.shape

'''time to build the model'''
Y = data[0:150,0]
X = data[0:150,1:]
model = linear_model.LogisticRegression(C=1e86)
fitted_model = model.fit(X,Y)
beta = fitted_model.coef_
intercept = fitted_model.intercept_
testX = data[150:,1:]
testY = data[150:,0]
predicted_Y = fitted_model.predict(testX)

