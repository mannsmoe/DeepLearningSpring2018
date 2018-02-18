from builtins import str

# creating a class named as Employees
class Employees:
    # Creating a constructor to initialize name, family, department
    def __init__(self,nm,fam,dprt):
        self.name = nm
        self.family = fam
        self.department = dprt


class Students:
    # Creating a constructor to initialize name, family, department
    def __init__(self,nm,fam,dprt):
        self.name = nm
        self.family = fam
        self.department = dprt
        

#Inheritance and using super to customize the inheritance
class FacultyMembers(Employees):
    # Creating a constructor to initialize name, family, department, and the field 
    def __init__(self,nm,fam,dprt,field):
        # Using super for single inheritance to allow adding new instances for the FacultyMembers class (which is field)
        super().__init__(nm,fam,dprt)
        self.major = field

        
class Librarieans:
    # Creating a constructor to initialize name, family, department
    def __init__(self,nm,fam,dprt):
        self.name = nm
        self.family = fam
        self.department = dprt

# Multi inheritance from Students, Employees,Librarieans classes and using the super constructor
class Books(Students, Employees,Librarieans):
    # Creating a constructor to initialize all the data members from all the multi-inheritance here 
    def __init__(self, auth, ttl, edi, field, nm, fam, dprt):
        Students.__init__(self, nm, fam, dprt)
        Employees.__init__(self, nm, fam, dprt)
        Librarieans.__init__(self, nm, fam, dprt)
        self.author = auth
        self.title = ttl
        self.edition = edi
        self.major = field
        self.__TempDepartment = dprt
     




# Adding 3 employees information into the Employees class
print("\n\nAdding 3 employees information into the Employees class : ")
EmployeeDataHolder = Employees("Josh", "Smith", "IT")
print("\n\n ===Employee #1===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee department : " + str(EmployeeDataHolder.department))
EmployeeDataHolder = Employees("Danny", "Smith", "Library")
print("\n\n ===Employee #2===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee department : " + str(EmployeeDataHolder.department))
EmployeeDataHolder = Employees("Sara", "Brown", "Registration")
print("\n\n ===Employee #3===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee department : " + str(EmployeeDataHolder.department))



# Adding 2 students information into the Students class
print("\n\nAdding 2 students information into the Students class : ")
StudentDataHolder = Students("Ahmed", "Albishri", "Computer Science")
print("\n\n ===Student #1===" + "\nStudent first name : " + str(StudentDataHolder.name) + "\nStudent family name : " + str(StudentDataHolder.family) + "\nStudent department : " + str(StudentDataHolder.department))
StudentDataHolder = Students("Khalid", "Almalki", "Telecommunication and Computer Networking")
print("\n\n ===Student #2===" + "\nStudent first name : " + str(StudentDataHolder.name) + "\nStudent family name : " + str(StudentDataHolder.family) + "\nStudent department : " + str(StudentDataHolder.department))




# Adding 2 Faculty Members information into the FacultyMembers class that is inherited from the Employees class and utilize the additional argument which is (the major).\n so we inheriting all the Employees class attributes using super() and adding the additional one:
print("\n\nAdding 2 Faculty Members information into the FacultyMembers class,\nwhich is inherited from the Employees class and add additional argument which is (the major).\nSo we customizing the inheritance here using super()\nThis additional attribute of the FacultyMembers class can be considered as a private data member")
FacultyMemberDataHolder = FacultyMembers("Alex", "Foard", "Computer Science", "Networking")
print("\n\n ===Faculty Member #1===" + "\nFaculty Members first name : " + str(FacultyMemberDataHolder.name) + "\nFaculty Members family name : " + str(FacultyMemberDataHolder.family) + "\nFaculty Members department : " + str(FacultyMemberDataHolder.department) + "\nFaculty Members field : " + str(FacultyMemberDataHolder.major))
FacultyMemberDataHolder = FacultyMembers("Matt", "Douglas", "Electrical Engineering", "Power Electronics")
print("\n\n ===Faculty Member #2===" + "\nFaculty Members first name : " + str(FacultyMemberDataHolder.name) + "\nFaculty Members family name : " + str(FacultyMemberDataHolder.family) + "\nFaculty Members department : " + str(FacultyMemberDataHolder.department) + "\nFaculty Members field : " + str(FacultyMemberDataHolder.major))



# Adding 2 Librarians information into the Librarieans class
print("\n\nAdding 2 Librarians information into the Librarians class : ")
LibDataHolder = Librarieans("Mike", "Allen", "Computer Science")
print("\n\n ===Librarian #1===" + "\nLibrarian first name : " + str(LibDataHolder.name) + "\nLibrarian family name : " + str(LibDataHolder.family) + "\nLibrarian department : " + str(LibDataHolder.department))
LibDataHolder = Librarieans("Michael", "Anderson", "Telecommunication and Computer Networking")
print("\n\n ===Librarian #2===" + "\nLibrarian first name : " + str(LibDataHolder.name) + "\nLibrarian family name : " + str(LibDataHolder.family) + "\nLibrarian department : " + str(LibDataHolder.department))



# Adding 2 books information into the Books class
print("\n\nAdding 2 Books information into the Books class : ")
BookDataHolder = Books("Corey Beard", "Wireless Communications", "2nd", "EECS", "Ahmed", "Albishri", "Computer Science")
print("\n\n ===Book title#1===" + "\nBook author : " + str(BookDataHolder.author) + "\nBook Title : " + str(BookDataHolder.title) + "\nBook Edition : " + str(BookDataHolder.edition) + "\nBorrowed by : " + str(BookDataHolder.name) + " " + str(BookDataHolder.family))
BookDataHolder = Books("Deep Medhi", "Network Routing", "3rd", "CS", "Khalid", "Almalki", "Telecommunication and Computer Networking")
print("\n\n ===Book title #2===" + "\nBook author : " + str(BookDataHolder.author) + "\nBook Title : " + str(BookDataHolder.title) + "\nBook Edition : " + str(BookDataHolder.edition) + "\nBorrowed by : " + str(BookDataHolder.name) + " " + str(BookDataHolder.family))




print("\n\nReteiving a private content form the Books class ...")
try:
    print(BookDataHolder.__TempDepartment)
except Exception:
    print("Error ! retrieving __TempDepartment failed because it is a private variable of Books class")
    print("\n\nCan't retrieve this private content from Books class")

    

