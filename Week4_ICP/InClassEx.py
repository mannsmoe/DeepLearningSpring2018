# creating a class named as Employees
class Employees:
    # Creating a class attributes used for the employees counting and salary average
    co = 0
    sal = 0
    # Creating a constructor to initialize name, family, salary, department
    def __init__(self,nm,fam,slr,dprt):
        self.name = nm
        self.family = fam
        self.salary = slr
        self.department = dprt
        # Creating a data member to count the number of the employees
        self.__class__.co = self.__class__.co + 1
        self.coun = self.__class__.co
        self.__class__.sal = self.__class__.sal + slr
        self.SumOfSalaries = self.__class__.sal
    # Creating a function to find the average salary of the employees   
    def SalaryAverage(self):
        self.SalariesAverage = self.SumOfSalaries/self.coun
        return self.SalariesAverage

# Create a Fulltime employees class and it should inherit the properties of Employees class
class Fulltime(Employees):
    pass


# Adding 3 employees information into the Employees class
print("\n\nAdding 3 employees information into the Employees class : ")
EmployeeDataHolder = Employees("Josh", "Smith", 5000, "IT")
print("\n\n ===Employee #1===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee salary : " + str(EmployeeDataHolder.salary)  + "\nEmployee department : " + str(EmployeeDataHolder.department))
EmployeeDataHolder = Employees("Danny", "Smith", 7000, "Library")
print("\n\n ===Employee #2===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee salary : " + str(EmployeeDataHolder.salary)  + "\nEmployee department : " + str(EmployeeDataHolder.department))
EmployeeDataHolder = Employees("Sara", "Brown", 9000, "Desk Support")
print("\n\n ===Employee #3===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee salary : " + str(EmployeeDataHolder.salary)  + "\nEmployee department : " + str(EmployeeDataHolder.department))


# Adding 3 employees information into the Fulltime class that is inherited from the Employees class
print("\n\nAdding 3 employees information into the Fulltime class that is inherited from the Employees class :")
EmployeeDataHolder = Fulltime("Alex", "Foard", 12000, "Computer Science")
print("\n\n ===Full Time Employee #1===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee salary : " + str(EmployeeDataHolder.salary)  + "\nEmployee department : " + str(EmployeeDataHolder.department))
EmployeeDataHolder = Fulltime("Matt", "Douglas", 15000, "Electrical Engineering")
print("\n\n ===Full Time Employee #2===" + "\nEmployee first name : " + str(EmployeeDataHolder.name) + "\nEmployee family name : " + str(EmployeeDataHolder.family) + "\nEmployee salary : " + str(EmployeeDataHolder.salary)  + "\nEmployee department : " + str(EmployeeDataHolder.department))


# Calling and printing the number of the employees
print("\n\nThe number of the employees is : " + str(EmployeeDataHolder.coun))



# Calling and printintg the average of the employees' salaries 
print("\n\nThe average of the employees' salaries is : " + str(EmployeeDataHolder.SalaryAverage()))

