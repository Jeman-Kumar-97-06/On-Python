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
    annual_raise = 1
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+last+'.email'
        Employeeyo.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self): #Regular method
        self.pay = int(self.pay + Employeeyo.annual_raise)
    @classmethod           #Class method
    def set_raise_amt(cls,amount):
        cls.annual_raise = amount

print("\n\n\nImportant Shit!")
empyo_1 = Employeeyo('Jeman','doe',50000)
empyo_2 = Employeeyo("Jack","Doe",60000)
'''
if you say ,
Employeeyo.set_raise_amt(2) --> it will change the annual_raise value of all the
empyo_1.set_raise_amt(2) --> It will do exactly what the above line did.

If you say,
Employeeyo.annual_raise = 10 --> it will do exactly what the above line did.
empyo_1.annual_raise = 10 --> This line will only change 'empyo_1''s 'annual_raise' value.
'''

print(empyo_1.pay)          #50000
Employeeyo.set_raise_amt(2)
empyo_1.apply_raise()
print(empyo_1.annual_raise)
print(empyo_1.pay)          #50002


Employeeyo.annual_raise = 1
empyo_1.apply_raise()       
print(empyo_1.pay)         #50002+1 = 50003

Employeeyo.set_raise_amt(2)
empyo_1.apply_raise()
print(empyo_1.pay)         #50003+2 = 50005
print("--------------------------\n\n\n")
#-------------------------------------------------
class Employeeyo_:
    num_of_emps = 0
    annual_raise = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        self.email = first+last+'.email.com'
        Employeeyo_.num_of_emps += 1
    def fullname(self): #a regular method --> 'self' as argument
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.annual_raise)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.annual_raise = amount
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first,last,pay)

emp_str_1 = 'Jeman-Doe-50000'
emp_str_2 = "Jack-Jane-60000"
new_emp_yo_1 = Employeeyo_.from_string(emp_str_1)
new_emp_yo_2 = Employeeyo_.from_string(emp_str_2)
print(new_emp_yo_1.__dict__)
print(new_emp_yo_2.__dict__)

#Example on Inheritance : 
print("\n\n\nINHERITANCE OUTPUT:")
class ParentEmployee:
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last 
        self.pay   = pay
        self.email = first+last+'.email.com'
    def fullname(self):
        print('{} {}'.format(self.first,self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class ChildEmployee(ParentEmployee):
    pass

cE_1 = ChildEmployee('Jeman',"Jack",50000)
cE_2 = ChildEmployee("Jane","Doe",60000)

print(cE_1.email) #JemanJack.email.com
print(cE_2.email) #JaneDoe.email.com

#----------------------------------

print(cE_1.pay)
class ChildEmployee2(ParentEmployee):
    raise_amount=1.10
cE_3 = ChildEmployee2("X","Y",50000)

cE_1.apply_raise()
cE_3.apply_raise()

print(cE_1.pay)
print(cE_3.pay)

#------------------------------------


class Manager(ParentEmployee):
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay) #Used to inherit 'first','last' and 'pay' from 'ParentEmployee'
        if (employees is None):
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            emp.fullname()

mgr_1 = Manager("Sue",'Smith',90000,[cE_1,cE_2])
print(mgr_1.email)
mgr_1.print_emps()


#isinstance() and issubclass() : 
print(isinstance(mgr_1,Manager))        #True
print(isinstance(mgr_1,ParentEmployee)) #True cuz it inherited shit
print(isinstance(mgr_1,ChildEmployee))  #False
print(issubclass(ChildEmployee,ParentEmployee)) #True
print(issubclass(Manager,ParentEmployee))   #True
print(issubclass(Manager,ChildEmployee)) #False