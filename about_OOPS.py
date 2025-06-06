#CLASS WITHOUT CONSTRUCTOR:
class StupidNumber:
    x = 5

y = StupidNumber()
print(y.x)

#CLASS WITH CONSTRUCTOR:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

p1 = Person('Jeman',61)
print(p1.name)
print(p1.age)

#__str__() function for string representation of an object:
class Animal:
    def __init__(self,limbs):
        self.limbs = limbs
    def __str__(self):
        return f"This object talks about no of limbs. The no of limbs here is {self.limbs}"
a1 = Animal(4)
print(a1)

#Object Methods:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age 
    def myFunc(self):
        print("Hello my name is : "+self.name)
p1 = Person("Jeman",61)
p1.myFunc()
#changing object props:
p1.age = 40
#delete object props:
del p1.age
#delete object:
del p1

#INHERITANCE:
#Child has same number of props as of the Parent:
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def speak(self):
        print(f"I am {self.name} and i make sounds")

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def speak(self):
        print("Woof Woof")

#Child has more Props that the Parent:
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def speak(self):
        print("I make a sound")

class Dog(Animal):
    def __init__(self,limbs,name,age):
        super().__init__(name,age)
        self.limbs=limbs