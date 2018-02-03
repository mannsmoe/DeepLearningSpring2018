
# Importing the used modules
import gc
# The list of numbers to be searched for the sum of threes
NumList = [3,2,-1,2,8,-2,9,4,-2,1,6,-4,-3,-6,10,16,13]
# Finding the length of the numbers list
NumListLength = len(NumList)
# Initializing the sum detection flag
Flag = True
# iterating through the list of the numbers three times, by adding any item in the list with a pair of other items each time
for i in range(0, NumListLength - 2):
    for j in range(i + 1, NumListLength - 1):
        for k in range(j + 1, NumListLength):
            if (NumList[i] + NumList[j] + NumList[k] == 0):
                print('The combination : (' + str(NumList[i]), str(NumList[j]), str(NumList[k]) + ')  gives a sum of zero')
                Flag = True
# If no combination was found
if (Flag == False):
    print(" No combination can give a sum of zero")
print('Exiting ...')
# Freeing up the used resources
del NumList 
del NumListLength 
del i
del j
del k
gc.collect()
print('End of the program, Thanks !')