# Importing the needed modules: numpy, pandas, sklearn, and matplotlib
# Importing numpy to deal with arrays
import numpy as np
# Importing pandas to deal with the dataset that is in CSV format
import pandas as pd
# Importing sklearn to use the machine learning tools: trining the data, fitting, implementing LDA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
# Importing matplotlib to plot the regression analysis results
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
# Loading the data
LoadedData = pd.read_csv('dataset.csv')
# The data
x = LoadedData.iloc[:, 0:9].values 
# The three groups members 1's, 2's, and 3's which is the last column in the data
y = LoadedData.iloc[:, 9].values
# Specifying the training vs testing data percentages 
print('Specifying the training vs testing data percentages: 40% Training and 60% Testing')
TrainingX, TestingX, TrainingY, TestingY = train_test_split(x, y, test_size = 0.4, random_state = 0)
# Fitting the training data
sc = StandardScaler()
TrainingX = sc.fit_transform(TrainingX)
TestingX = sc.transform(TestingX)
# Applying LDA
LDAClass = LDA(n_components = 2)
TrainingX = LDAClass.fit_transform(TrainingX, TrainingY)
TestingX = LDAClass.transform(TestingX)
# Testing the trained results 
RegClass = LogisticRegression(random_state = 0)
RegClass.fit(TrainingX, TrainingY)
TestingResult = RegClass.predict(TestingX)
cm = confusion_matrix(TestingY, TestingResult)

# Plotting the Training results
xCoordinates, yCoordinates = TrainingX, TrainingY
HorizStart, HorizEnd = np.meshgrid(np.arange(start = xCoordinates[:, 0].min() - 1, stop = xCoordinates[:, 0].max() + 1, step = 0.005),
                     np.arange(start = xCoordinates[:, 1].min() - 1, stop = xCoordinates[:, 1].max() + 1, step = 0.005))
plt.contourf(HorizStart, HorizEnd, RegClass.predict(np.array([HorizStart.ravel(), HorizEnd.ravel()]).T).reshape(HorizStart.shape),
             alpha = 0.75, cmap = ListedColormap(('black', 'red', 'green')))
plt.xlim(HorizStart.min(), HorizStart.max())
plt.ylim(HorizEnd.min(), HorizEnd.max())
for a, b in enumerate(np.unique(yCoordinates)):
    plt.scatter(xCoordinates[yCoordinates == b, 0], xCoordinates[yCoordinates == b, 1],
                c = ListedColormap(('black', 'red', 'green'))(a), label = b)
plt.title('Training Results for the Three Classes')
plt.xlabel('Training x')
plt.ylabel('Training y')
plt.legend()
plt.show()
#Plotting the Testing results
xCoordinates, yCoordinates = TestingX, TestingY
HorizStart, HorizEnd = np.meshgrid(np.arange(start = xCoordinates[:, 0].min() - 1, stop = xCoordinates[:, 0].max() + 1, step = 0.005),
                     np.arange(start = xCoordinates[:, 1].min() - 1, stop = xCoordinates[:, 1].max() + 1, step = 0.005))
plt.contourf(HorizStart, HorizEnd, RegClass.predict(np.array([HorizStart.ravel(), HorizEnd.ravel()]).T).reshape(HorizStart.shape),
             alpha = 0.75, cmap = ListedColormap(('black', 'red', 'green')))
plt.xlim(HorizStart.min(), HorizStart.max())
plt.ylim(HorizEnd.min(), HorizEnd.max())
for a, b in enumerate(np.unique(yCoordinates)):
    plt.scatter(xCoordinates[yCoordinates == b, 0], xCoordinates[yCoordinates == b, 1],
                c = ListedColormap(('black', 'red', 'green'))(a), label = b)
plt.title('Testing Results for the Three Classes')
plt.xlabel('Testing x')
plt.ylabel('Testing y')
plt.legend()
plt.show()

