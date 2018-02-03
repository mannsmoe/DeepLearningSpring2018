
# Importing the used modules
import gc
# The lists of the students names for both classes
PythonStudents = ["Abdoh", "Erick", "Stive", "Moe", "Susan", "Sarah","Helen", "Harry", "Mark", "Josh", "Shon"]
WebAppStudents = ["Aaron", "Moe", "Maria", "Josh", "Erick", "A", "Susan", "Mark", "Jim", "Brendan", "Shon", "Paul", "Barry", "Julia"]
print("")
# printing the students names who are found in both classes, by iterating in both of the names lists
print('Students who are in both classes : ')
for PythonStudent in PythonStudents:
    for WebAppStudent in WebAppStudents:
        # The condition where a student is found in both classes
        if PythonStudent == WebAppStudent:
            print(PythonStudent)

print("")
print('=========================')
print("")
print('Students who are not common in both the classes : ')
# Initializing the detection indicator value
Indicator=0
for PythonStudent in PythonStudents:
    for WebAppStudent in WebAppStudents:
        if PythonStudent == WebAppStudent:
            # If each name in the first students group has a match in the second students group 
            # then we set the indicator to 1 to not include this name in the not common list of names 
            Indicator=1
    # If a match discovered (indicator=1) then we will not print this name 
    # and we will reset the indicator back to its original value (0) to compare 
    # the next name from the fist group with all the names of the second group
    if Indicator==1:
        Indicator=0
    # If no match found then this student is not common in both classes, so we print his/her name
    elif Indicator==0:
        print(PythonStudent)

print("")
print('Exiting ...')
# Freeing up the used resources
del PythonStudents 
del WebAppStudents
gc.collect()
print('End of the program, Thanks !')