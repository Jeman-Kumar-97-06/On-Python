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

#Example : Using NO Class Attributes:
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

#Example : Using Class Attributes:
class Employee__:
    annual_raise = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+last+'.email'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * Employee__.annual_raise)
        # self.pay = int(self.pay*self.annual_raise) #--> 0 fucks

employee___1 = Employee__("Jeman","Jane",50000)
employee___2 = Employee__("Jeevan","Doe",60000)

print(employee___1.__dict__) #U won't see 'annual_raise' here
print(Employee__.__dict__) # U will see 'annual_raise' here

print(employee___1.pay)
employee___1.apply_raise()
print(employee___1.pay)

employee___1.pay = 50000
print(employee___1.pay)
Employee__.annual_raise = 1.06
employee___1.apply_raise()
print(employee___1.pay)

#Another Example with class attributes : 
class Employee___:
    num_of_emps = 0
    annual_raise = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.email = first+last+'.email'
        Employee___.num_of_emps +=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*self.annual_raise)

print(Employee___.num_of_emps)

employee____1 = Employee___("Jeman","KUmar",50000)

print(Employee___.num_of_emps)

#Examples showing regular vs class vs static methods:
class Employeeyo:
    num_of_emps = 0
    annual_raise = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+last+'.email'
        Employeeyo.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay*self.annual_raise)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.annual_raise = amount

empyo_1 = Employeeyo('Jeman','doe',50000)
Employeeyo.set_raise_amt(1.05)

#-------------------------------------------------
class Employeeyo_:
    num_of_emps = 0
    annual_raise = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first + last + '.email'
        Employeeyo_.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.annual_raise)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.annual_raise = amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_str_1 ="John-Doe-50000"
emp_str_2 ="Jane-DOe-60000"
