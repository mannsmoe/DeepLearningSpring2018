# Lab #2 Requirement #1

# Initializing the minimum possible price as 0
UserRangeMin = 0
# Sking the user to enter their min and max price range 
print('Please enter your price range. Minimum Range is zero default ..')
UserRangeMin=input('Min : ')
UserRangeMax=input('Max : ')
# Books names and prices in a dictionary format
Books = { "Wireless": 220, "Networking": 140, "Data Structure": 80, "Linux Server Admin": 260 \
         , "Client Server Programming with linux": 285}
print('The book(s) that in the range of $' + str(UserRangeMin) + ' and $' + str(UserRangeMax) + ' is/are : ')
# Iterating through the dictionary and checking the value part (the book price) and print the matching book name and price
for key in Books:
    if Books[key] >= int(UserRangeMin) and Books[key] <= int(UserRangeMax):
        print('The book ('+ str(key) +') has a price of $' + str(Books[key]))