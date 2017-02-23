#Kyle Verdeyen
#CG:DA PSET1
#Feb 2017
#Assumes necessary files are in same directory as script
from sklearn import linear_model
import numpy as np
import sys

#usint only 1st 10 genes
#read & form second column of phen_train  file
phen_train = np.genfromtxt('phen_train.csv', delimiter=',', skip_header=1, usecols=(1))
phen_train.shape

#read & form train_expression
train_expression = np.genfromtxt('train_expression.csv', max_rows=10, delimiter=',', skip_header=1, usecols=range(1,146))
train_expression.shape

#Y is our discrete "basilar or luminal"
Y = phen_train[0:145]
#X is data
X = train_expression[0:,0:]
#model, c=2 because this is a binary classification
model = linear_model.LogisticRegression(C=2)
fitted_model=model.fit(X.reshape(145,10),Y)
#coefficients (beta)
beta = fitted_model.coef_
#intercept (bias)
intercept = fitted_model.intercept_

#compare vs target data
phen_test = np.genfromtxt('phen_test.csv', delimiter=',', skip_header=1, usecols=(1))
test_expression = np.loadtxt('test_expression.csv', delimiter=',', skiprows=1, usecols=range(1,11), ndmin=2)
predicted_Y = fitted_model.predict(test_expression)
print("Actual test data:")
print(phen_test)
print("Predicted test data:")
print(predicted_Y)
print("Bias: ")
print(intercept)
print("Coefficients:")
print(beta)
