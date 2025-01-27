#Kyle Verdeyen
#Computational Genomics Data Analysis
#Problem set 4, exercise 4
#Usage: python problem_4.py phen_train.csv phen_test.csv train_expression.csv test_expression.csv
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import normalize
from scipy import stats

phen_train = np.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, usecols=(1), dtype='float')
#phen_train = stats.zscore(phen_train)
train_expression = np.loadtxt(sys.argv[3], delimiter=',', skiprows=1, usecols=range(1,146), ndmin = 2, dtype='float')
train_expression = stats.zscore(train_expression)
phen_test = np.genfromtxt(sys.argv[2], delimiter=',', skip_header=1, usecols=(1), dtype='float')
#phen_test = stats.zscore(phen_test)
test_expression = np.loadtxt(sys.argv[4], delimiter=',', skiprows=1, usecols=range(1,51), ndmin=2, dtype='float')
test_expression = stats.zscore(test_expression)
X = train_expression.T
Y = phen_train
A = test_expression.T
B =  phen_test
#50 neuron layers, hidden_layer_sizes takes a tuple of #of neurons for # of layers
one = (50)
two = (50,50)
sixteen = (50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50)
thirtytwo = (50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50)
relu = []
logistic = []


#ex 4.1
#constant random_state=2...no idea if this is a good seed but we're rolling with it
#new mlp, set params, fit, predict test set, calculate error. repeat for 8
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
print('Iter = 10000:')
print('RELU errors:',relu)
print('logistic errors:', logistic)

#now we have fit, predicted, and calculated the error for all 8
#now plot
#plot for relu
plt.figure()
graphX = [1,2,16,32]
graphY = relu
plt.title('Error for RELU')
plt.plot(graphX, graphY)
plt.show()

#plot for logistic
plt.figure()
graphY = logistic
plt.title('Error for Logistic')
plt.plot(graphX, graphY)
plt.show()



#4.2: see problem4_answers



#4.3: iter=200
relu = [] #reset collection
logistic = []
mlp = MLPClassifier(hidden_layer_sizes=one, activation='relu', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=two, activation='relu', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=sixteen, activation='relu', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=thirtytwo, activation='relu', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
relu.append(error)
mlp = MLPClassifier(hidden_layer_sizes=one, activation='logistic', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
mlp = MLPClassifier(hidden_layer_sizes=two, activation='logistic', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
mlp = MLPClassifier(hidden_layer_sizes=sixteen, activation='logistic', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
mlp = MLPClassifier(hidden_layer_sizes=thirtytwo, activation='logistic', random_state=2, max_iter=200)
mlp.fit(X,Y)
prediction = mlp.predict(A)
error = np.mean(prediction != B)
logistic.append(error)
print('Iter = 200:')
print('RELU errors:',relu)
print('logistic errors:', logistic)

#relu plot iter=200
plt.figure()
graphX = [1,2,16,32]
graphY = relu
plt.title('Error for RELU')
plt.plot(graphX, graphY)
plt.show()

#logistic plot iter=200
plt.figure()
graphY = logistic
plt.title('Error for Logistic')
plt.plot(graphX, graphY)
plt.show()
