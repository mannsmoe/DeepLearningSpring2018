
# Importing the used modules
import re
import gc
# Initializing the conditions flag
flag = True
# Running a loop to ask the user to enter their input again or exit
while flag:
    # Asking the user to input the password
    password= input("Input your password : ")
    # Finding the password length
    PasswordLength=len(password)
    # Testing if the password satisfy the length condition that is in range of 6 to 16
    if (PasswordLength<6 or PasswordLength>16):
        print("Invalid password ! The password must be in range of 6 to 16 charcters")
        flag=False
     # Testing if the password contains lower case letter
    elif not re.search("[a-z]",password):
        print("Invalid password ! The password must contain a lower case letter")
        flag=False
    # Testing if the password contains upper case letter
    elif not re.search("[A-Z]",password):
        print("Invalid password ! The password must contain an upper case letter")
        flag=False
    # Testing if the password contains numbers
    elif not re.search("[0-9]",password):
        print("Invalid password ! The password most contain a number")
        flag=False
    # Testing if the password contains special character
    elif not re.search("[$@!*]",password):
        print("Invalid password ! The password must contain one special character")
        flag=False
    # If none of the above tests had met then we have to set the flag value to True which means the password met all the requirements
    elif flag==True:
        print("Great ! it is a valid password")
    # Loop control to see if the user wants to check another password or just quitting the program
    print('Do you want to check another password? y = YES, n  NO and exit')
    decision=input('Your answer: ')
    if decision=='n': 
        flag=False
        print('Thank you for using Password Checker! Exiting ...')
    else:
        flag=True
        #break
# Freeing up the used resources
del password
gc.collect()
print("Password Checker is closed")
