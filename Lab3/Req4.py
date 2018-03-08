# Importing the needed dependencies: sklearn
# Importing sklearn to use the machine learning components
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.cross_validation import train_test_split

# Loading the data
print('\n\nLoading the iris dataset ...')
irisdataset = datasets.load_iris()
Entries = irisdataset.data
Responses = irisdataset.target
# Specifying the training vs testing data percentages
print('\n\nSpecifying the training vs testing data percentages: 20% Training and 80% Testing ...')
TrainingX, TestingX, TrainingY, TestingY = train_test_split(Entries, Responses, test_size = 0.2)

# Fitting the training data
K = 1
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('\nFor K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))



K = 2
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))


K = 5
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))



K = 10
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))



K = 40
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))




K = 50
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))



K = 60
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))




K = 70
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))




K = 80
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))



K = 90
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))


K = 100
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))



K = 110
KNNTemp = KNeighborsClassifier(n_neighbors = K)
KNNTemp.fit(TrainingX,TrainingY)
# Testing the results
Testingresult = KNNTemp.predict(TestingX)
print('For K = ' + str(K) + ', the accuracy is : ' + str(metrics.accuracy_score(TestingY,Testingresult)))


print('\n\n Conclusion: It is very clear that the accurace maintain a high value as K is from 1 to around 70.')
print('After K = 70, the accuracy is dropping dramatically')

