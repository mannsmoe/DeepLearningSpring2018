# Importing the required modules 
import numpy as np
# Generating a vector of 15 random values between 0 and 20 
RandArray = np.random.randint(20, size = 15)
print("The randomly generated array:", RandArray)
# Finding the most frequent element in this vector
MostFrequent = np.bincount(RandArray).argmax()
print("Most frequent element in this vector is : ", MostFrequent)
