
# Importing the used modules
import math
import gc
# Asking the user to input the sentence
sentence=input('Enter a sentence here : ')
# Converting the sentence from string to list of words
SentenceAsList=sentence.split()
# Finding the list length
SentenceLength=len(SentenceAsList) #measuring the list length
# Checking if the list contains even number of words, so we need to find two middle words
if SentenceLength % 2 == 0:
    MiddleWordPosition=math.floor(SentenceLength/2)-1 #Flooring the half of the list
    # Finding the position of the two middles
    MiddleWordPosition2=MiddleWordPosition+1
    FirstMiddleWord=SentenceAsList[MiddleWordPosition]
    SecondMiddleWord=SentenceAsList[MiddleWordPosition2]
    print('First middle word is : ' + FirstMiddleWord)
    print('Second middle word is : ' + SecondMiddleWord)
    print('=========')
    print('')
else:
    # If the number of the words in the sentence list is odd, then there will be only one middle word
    MiddleWordPosition=SentenceLength/2
    MiddleWord=SentenceAsList[math.floor(MiddleWordPosition)]
    print('The middle word is : ' + MiddleWord)
    print('=========')
    print('')

# Finding the word of the maximum length
print ('The longest word in the sentence is : ' + max(sentence.split(), key=len))
print('=========')
print('')
# Printing the sentence in reverse order
print('The sentence with reverse words and letters is : ' + sentence[::-1])
print('Exiting ...')
# Freeing up the used resources
del sentence 
del SentenceAsList 
del SentenceLength
gc.collect()
print('End of the Program, Thanks ...')