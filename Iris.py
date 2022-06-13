# -*- coding: utf-8 -*-
"""IrisML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z322A82oJc0x7peS2f8zMaQBp4d7aX2L
"""

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#import and load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal_length', ' sepal_width','petal_length','petal_width','class']
dataset = read_csv(url, names=names)

#shape (rows,columns)
print("Size: \n")
print(dataset.shape)
print()

#top 20 rows head
print("head(20)\n")
print(dataset.head(20))
print()

#description - statistic information
print("Desctibe stats\n")
print(dataset.describe())
print()

#distribution by class
print("Size by grouping:\n")
print(dataset.groupby('class').size())
print()

dataset.plot(kind ='box', subplots =True, layout = (2,2), sharex = False, sharey=False)
pyplot.show()

dataset.hist()
pyplot.show()

scatter_matrix(dataset)
pyplot.show()
#--------------------------------------------
array = dataset.values
x = array[:, 0:4]
y = array[:, 4]
x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size =0.20, random_state=1)
print(len(y_validation))

from numpy.ma.core import append
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class ='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

results = []
names = []
for name, model in models:
  kfold = StratifiedKFold(n_splits=10, random_state =1, shuffle = True)
  cv_results = cross_val_score(model,x_train,y_train,cv=kfold,scoring = 'accuracy')
  results.append(cv_results)
  names.append(name)
  print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

pyplot.boxplot(results,labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

model = SVC(gamma='auto')
model.fit(x_train, y_train)
predictions = model.predict(x_validation)

print(accuracy_score(y_validation, predictions))
print(confusion_matrix(y_validation, predictions))
print(classification_report(y_validation, predictions))