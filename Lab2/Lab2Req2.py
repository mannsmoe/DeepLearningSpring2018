# Importing the used modules
import gc
# The nested list/dictionary information of the contacts which contains name, phone number, and email address
list1={"Moe":['Moe','8162352222','mkakh3@mail.umkc.edu'], "Mike":['Mike', '8168927366', 'sdlk@mail.umkc.edu']}
# An infinite loop to keep asking the user to enter their choice
while True:
    # The available options that a user can use 
    print('To display contact by name press 1\nTo display contact by number press 2\nTo edit contact by name press 3\nTo quit the program press 4')
    indexx = input('your selection is : ')
    # A glag to indicate if the user entered a name that is not in the contacts list so it give an error saying that
    flagg = 0
    # The case when the user enters 1 to search and display contact info by name
    if indexx == str(1):
        name1 = input('Enter a name to display its contact : ')
        for key in list1:
            if key == name1:
                flagg = 1
                print('Name   : ', list1[name1][0])
                print('Number : ', list1[name1][1])
                print('Email  : ', list1[name1][2])
        if flagg == 0:
            print('Ooops ! This name can not be found, try again !')
    elif indexx == str(2):
        # The case when the user enters 2 to search and display contact info by number
        num = input('Enter a number to display its contact : ')
        for key in list1:
            if list1[key][1] == num:
                flagg = 1
                print('Name   : ', list1[key][0])
                print('Number : ', list1[key][1])
                print('Email  : ', list1[key][2])
        if flagg == 0:
            print('Ooops ! This name can not be found, try again !')
    elif indexx == str(3):
        # The case when the user enters 3 to search and edit contact info by number
        name1 = input('Enter a name to modify its contact info : ')
        for key in list1:
            if key == name1:
                flagg = 1
                # User have to specify to edit the number (select n) or the email (select e)
                print('Enter n to modify the number or e to modify the email ...')
                indexxx = input('your selection is : ')
                if indexxx == 'n':
                    # Asking for the new number and changing it
                    NewNumber = input('The new number is : ')
                    list1[name1][1] = NewNumber
                elif indexxx == 'e':
                    # Asking for the new email and changing it
                    NewEmail = input('The new email is : ')
                    list1[name1][2] = NewEmail
                print('\nThe updated list of contact is: ')
                for key in list1:
                    print('Name   : ', list1[key][0])
                    print('Number : ', list1[key][1])
                    print('Email  : ', list1[key][2])
                    print('\n')
        if flagg == 0:
            print('Ooops ! This name can not be found, try again !')
    elif indexx == str(4):
        # when user enters 4 to exit
        print('Exiting the Contact List program ...')
        print("")
        print('Exiting ...')
        # Freeing up the used resources
        del list1 
        gc.collect()
        print('End of the program, Thanks !')
        break
    else:
        # when user enters anything not 1,2,3,4
        print('Error ! you have to enter 1, 2, 3, or 4')
            


        



"""
Copyright (C) Moe Mans All Rights Reserved. 
Any unauthorized usage or copying of this file via any medium is totally prohibited.

"""