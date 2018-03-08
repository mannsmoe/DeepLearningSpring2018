# Importing the needed dependencies: re, collections, and nltk
# Importing sklearn to use the machine learning components
import re, collections
from nltk.tokenize import wordpunct_tokenize, sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer


def tokens(text):
    return re.findall('[a-z]+', text.lower())


WordsList=[]

# Reading the text file: TheTaleofPeterRabbit.txt
print('\n\nReading the text file: TheTaleofPeterRabbit.txt ...')
TextFile = open('TheTaleofPeterRabbit.txt').read()
print('Converting the text into words (Tokenizing it) ...')
TextFileAsWords = tokens(TextFile)

# Applying Lemmatization on the words:
print('\n\nApplying Lemmatization on the words ...')
LemmatizedWords = WordNetLemmatizer()
for i in TextFileAsWords:
    WordsList.append(LemmatizedWords.lemmatize(i, pos = 'v'))

# Applying the bigram and calculating the words frequency
print('\n\nApplying the bigram and calculating the words frequency ...')
WordsClass = []
ClassifiedWordsList = pos_tag(WordsList)
frequency = 0
TempIteration = 0  
FrequentWordHolder = []  
while frequency<len(ClassifiedWordsList):
    if ClassifiedWordsList[frequency][1] != 'VB' or ClassifiedWordsList[frequency][1] != 'VBD' or ClassifiedWordsList[frequency][1] != 'VBG' or ClassifiedWordsList[frequency][1] != 'VBN' or ClassifiedWordsList[frequency][1] != 'VBP' or ClassifiedWordsList[frequency][1] != 'VBZ':
        WordsClass.append(ClassifiedWordsList[frequency])
    frequency +=1

Frequencies = collections.Counter(WordsClass)
print('Words frequencies is : ', Frequencies)

# Choosing the top five bi-grams that has been repeated most:
print('\n\nFinding the top five bi-grams that has been repeated most ...')
TopFiveFrequent = Frequencies.most_common(5)
print('The top five frequent words are : ', TopFiveFrequent)

while TempIteration<len(TopFiveFrequent):
    FrequentWordHolder.append(TopFiveFrequent[TempIteration][0][0])
    TempIteration +=1
print(FrequentWordHolder)

# Going through the original text and finding all the sentences with those most repeated bi-grams:
print('\n\nGoing through the original text and finding all the sentences with those most repeated bi-grams ...')
TextFile2 = open('TheTaleofPeterRabbit.txt').read().lower()
TextFile2Sentences = sent_tokenize(TextFile2)
SentencesList = []
# Extracting the sentences and concatenating them
print('\n\nExtracting the sentences and concatenating them ...')
for i in TextFile2Sentences:
    SentencesAsWords = word_tokenize(i)
    for j in SentencesAsWords:
        if j in FrequentWordHolder:
            SentencesList.append(i)
        break
print ('The concatenated sentences : ', SentencesList)