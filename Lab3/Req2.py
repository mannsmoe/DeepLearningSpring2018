# Importing the needed dependencies: sklearn module
# Importing sklearn to use the machine learning components
from sklearn.cross_validation import train_test_split
from sklearn import svm, datasets, metrics
# Loading digits dataset from sklearn module
print('Loading Digits dataset from sklearn module ...')
DigitsLoaded = datasets.load_digits()
Entry = DigitsLoaded.data
Response = DigitsLoaded.target
# Specifying the training vs testing data percentages
print('\nSpecifying the training vs testing data percentages: 40% Training and 60% Testing ...')
TraningX, TestingX, TrainingY, TestingY = train_test_split(Entry, Response, test_size = 0.4)
# Applying CVS with Linear Kernel
print('\nApplying SVC with Linear Kernel ...')
SVCLinearKernel = svm.SVC(kernel = 'linear', C = 1, gamma = 1)
# Fitting the training data
SVCLinearKernel.fit(TraningX,TrainingY)
# Testing the results
TestingResults = SVCLinearKernel.predict(TestingX)
print ('The accuracy score of the SVC with Linear Kernel = ',metrics.accuracy_score(TestingY,TestingResults))
# Applying the SVC with RBF kernel
print('\nApplying the SVC with RBF kernel ...')
SVCRBF =svm.SVC(kernel = 'rbf', C = 1, gamma = 1)
# Fitting the training data
SVCRBF.fit(TraningX,TrainingY)
# Testing the results
TestingResults = SVCRBF.predict(TestingX)
#checking the accuracy of the model with digits datasets by rbf kernel
print ('The accuracy score of the SVC with RBF = ',metrics.accuracy_score(TestingY,TestingResults))