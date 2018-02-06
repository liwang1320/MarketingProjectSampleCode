import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn import linear_model
from sklearn import tree
from sklearn import naive_bayes
from sklearn import ensemble

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

from parseData import parseAllRemoveIncomplete
from parseTreatedData import getTreatedX


def split_train_test(X, y, ratio, is_random = 0, seed = 0):
    if is_random:
        X_train, X_test, y_train, y_test = train_test_split(X, 
        y, test_size = ratio, random_state = seed)
    else:
        n_samples, n_features = np.mat(X).shape
        n_train = int(n_samples * ratio)
        X_train = X[:-n_train]
        X_test = X[-n_train:]
        y_train = y[:-n_train]
        y_test = y[-n_train:]
    return X_train, X_test, y_train, y_test

def cross_val(X, Y):
	# problem_type = 1 for regression, 0 for classification
	ratio = 0.3
	X_train, X_test, y_train, y_test = split_train_test(X, Y, ratio, is_random = 0, seed = 0)

	model = linear_model.LogisticRegression(penalty = 'l2')
	cls = model.fit(X, Y)
	test_score = cls.score(X_test, y_test)
	print("these are the coefficients")
	print(list(cls.coef_))
	print("these are the model params")
	print(cls.get_params())
	print("\n")
	print("this is cross validation score ")


	print(cross_val_score(cls, X, Y, cv = 5))
	return test_score
# print(parseAllRemoveIncomplete())

#return the number of times more positives there are in newPositive than old positive
def countPercentageIncrease(oldPositive, newPositive):
	oldPositiveTotal = 0
	for i in oldPositive:
		if i==1:
			oldPositiveTotal+=1
	newPositiveTotal = 0
	for j in newPositive:
		if j==1:
			newPositiveTotal+=1

	print("new number of adopters: ")
	print(newPositiveTotal)

	print("old number of adopters: ")
	print(oldPositiveTotal)
	return float(newPositiveTotal)/oldPositiveTotal

def predictUsingModel(X, Y, newX):
	model = linear_model.LogisticRegression(penalty = 'l2')
	cls = model.fit(X, Y)

	newY = model.predict(newX)
	oldY = model.predict(X)


	return "Number of times of adopter increase: " + str(countPercentageIncrease(oldY, newY) - 1)


X,Y = parseAllRemoveIncomplete()
newX = getTreatedX()

print(predictUsingModel(X, Y, newX))

# cross_val(X,Y)





