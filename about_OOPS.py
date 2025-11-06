#Example1 --> Only declaration, no initialization:
class Emp:
    pass

emp_1 = Emp()
emp_2 = Emp()

print(emp_1) #location x
print(emp_2) #location y

emp_1.first = "Corey"
emp_2.email = "Jack@gmail.com"

emp_2.first = 'Jane'
# emp_2.email = "Doe@gmail.com"

print(emp_1) #location x
print(emp_2) #location y

#Example2 : Define a class with instance variables:
class Employee:
    def __init__(self,first,last,pay):
        self.first = first #instance variable
        self.last  = last  #instance variable
        self.pay   = pay   #instance variable
    def fullname(self):
        print (f'{self.first} {self.last}')

employee_1 = Employee('Jeman',"Kumar",50000) #instance of a class-Obj
employee_1.fullname()
Employee.fullname(employee_1)

#Example : Using Class Attributes:
class Employee_:
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + last + '.email'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)

employee__1 = Employee_("Jeman","Kumar",50000)
employee__2 = Employee_("Jane",'Doe',60000)

print(employee__1.pay)
employee__1.apply_raise()
print(employee__1.pay)