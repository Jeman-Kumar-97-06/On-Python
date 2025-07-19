#Taking input : 
#Ex 1:
print("Enter your name : ")
name = input()
print(f"Hello {name}")
#Ex 2:
name = input("Please enter:")
print(name)

#Type Conversion (TypeCasting) : 

num = 12345
#print(len(num)) will give error.
print(len(str(num)))

print(type(num))#--> <class 'int'>

print(int('123')+int('123'))

#print(int('123')+'456') gives error

print(bool(1)) #Gives True

print(str(123))

print(float(123)) #Gives 123.0

print(int(12.5)) #Gives 12

print("Number of letters in your name is : "+len(input("Enter your name"))) #Error
print("Number of letters in your name is : "+str(len(input("Enter your name")))) #Now no error