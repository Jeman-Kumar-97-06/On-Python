#Taking input : 
#Ex 1:
print("Enter your name : ")
name = input()
print(f"Hello {name}")
#Ex 2:
name = input("Please enter:")
print(name)

#Type Conversion : 

num = 12345
#print(len(num)) will give error.
print(len(str(num)))

print(type(num))#--> <class 'int'>