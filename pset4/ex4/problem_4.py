#Kyle Verdeyen
#Computational Genomics Data Analysis
#Problem set 4, exercise 4
#Usage: python problem_4.py phen_train.csv phen_test.csv train_expression.csv test_expression.csv
import sys
import numpy as np
from sklearn.neural_network import MLPClassifier

phen_train = np.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, usecols=(1))
train_expression = np.loadtxt(sys.argv[3], delimiter=',', skiprows=1, usecols=range(1,146), ndmin = 2)
phen_test = np.genfromtxt(sys.argv[2], delimiter=',', skip_header=1, usecols=(1))
test_expression = np.loadtxt(sys.argv[4], delimiter=',', skiprows=1, usecols=range(1,51), ndmin=2)
X, Y = train_expression.T, phen_train
A, B = test_expression.T, phen_test
one = (50)
two = (50,50)
sixteen = (50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50)
thirtytwo = (50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50)
relu = []
logistic = []
#ex 4.1
#constant random_state=2...no idea if this is a good seed but we're rolling with it
mlp = MLPClassifier(hidden_layer_sizes=one, activation='relu', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=two, activation='relu', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=sixteen, activation='relu', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=thirtytwo, activation='relu', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=one, activation='logistic', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
mlp = MLPClassifier(hidden_layer_sizes=two, activation='logistic', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
mlp = MLPClassifier(hidden_layer_sizes=sixteen, activation='logistic', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
mlp = MLPClassifier(hidden_layer_sizes=thirtytwo, activation='logistic', random_state=2, max_iter=10000)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
print(relu)
print(logistic)
