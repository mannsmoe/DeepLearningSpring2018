
# DeepLearningSpring2018
Author:
Moe Almansoori

Objective: 
Being familiar with the basic functions and tools of Python by solving simple text processing problems. Such as indexing a string, converting a string to a list separate words, searching and testing some conditions. So, we went through four different tasks.
The objective for each task:
1-	Creating a password validation tool: This tool must check whether the password satisfies specific conditions which is very important and popular requirement when selecting a password to ensure it is a strong one and it is hard to compromise. This task gave an opportunity to use if statement and how to test if a string contains one of s group of characters.
2-	Identifying the middle word and the longest word in a string and reversing a string: This task focuses on how to index a string by converting it to a list of words. Here we are dealing with lists and how to access specific element in the list using its position. Other thing is how to iterate within a string in both straight and reverse ways.
3-	Finding the zero sum for three elements within a list of numbers. This is more like an algorithms problem as we have to iterate this numbers list almost three times to keep testing combinations of three numbers. This task gives about sequential iteration within in specific pattern i.e. selecting two numbers from the list each time and adding it to a third number from the same list and test whether the result equals zero. This application can be useful in many cases like load balancing problems and monitoring a system if its values accedes specific level or margin.
4-	Searching for common names in two different names lists: Here the program is looking for the common names in two classes enrolment lists. Such application is popular and important such as the one needed in final exams scheduling or task assigning where we need to avoid time or task conflict. The program is using loops to iterate through the loops and the if statement to test the matching possibility.


Features:
The accomplished programs have been written in a simple programming structure and considering the logic sequence in results processing and proper transitioning between the steps. It is considered that when someone else reads the program to understand its commands line by line and or blocks functionality, by clearly separating the tasks and giving descriptive names for the variables and providing descriptive comments for the main parts of the code.


Configuration:
Similar working configuration had been used for all the Lab1 requirements, they are:
Python 3.6
OS: Widows 10
IDE: Eclipse 


The implementation including code snippet
Requirement 1:
The program asks the user to enter their password to test it whether the it contains lower case letters, upper case letters, numbers, and special characters. Also, the program tests weather the password length in the range of 6 to 16 characters.
 The program is running an interactive while loop which keep asking the user to exit after finishing the test or testing another password.
Finally, the program frees the memory that has been used

Requirement 2:
The program asks the user to enter their string and then it converts this string to a list of words using split() function. To find the middle word in this word list the program counts the words by finding the list length and divide it by 2. When the list length is odd we will ceil/round (ignoring the division reminder) the result and this result will be the position of the middle word. However, if the length of the list Is a even number then we will be having two middles; upper and lower. The lower is the word of the position of the half of the list length and the upper middle is the one if the next position to the lower.
To find the longest word in this list we use max() function. Finally, to reverse the string, we iterate it from the end to the beginning be using the negative index. Lastly, the program frees the memory that has been used

Requirement 3:
Here the program is searching for any three numbers in a list of number in which their sum is zero. The program uses three loops to iterate through the list by selecting two numbers each time and add them to all of the list numbers and test whether their sum is equal to zero.

Requirement 4:
Here the program is testing two groups of student’s names that are enrolled in two different classes. It searches for the common students who have been enrolled for both classes. Also, it searches for the student that are not taking both classes.
The program is using tow loops to compare each student name in the first group with all the names of the second group.




Explain about the deployment
It started with understanding the problem and figuring out what a good way to provide the required results. Then writing down a pseudo code and what is the input type and format. I was trying to avoid using any unnecessary programming structures and seek the simplicity. The startup program can be containing unnecessary loops or variables, but with several testing and polishing the code, the programs because more effective and easy to follow and understand.


Limitation
The programs that been developed for this lab purpose still need more improvements to serve in real life environment. For example, the password program need to check if a space been used and give a warning for that. Other thing is these programs does not save the results permanently such as in a file.



References
1-	https://docs.python.org/3/reference/import.html
2-	https://docs.python.org/3/library/functions.html#max
3-	https://pymotw.com/2/gc/
4-	https://docs.python.org/3/library/gc.html
5-	https://github.com/tensorflow/tensorflow/issues/1727
