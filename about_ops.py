#ARITHMETIC OPERATORS : 
print('2'+'jeman')
print(2 * 'jeman')

# print('jeman'-'n')
print(10-1)

print(10/3) #Gives 3.333
print(10//3) #Gives 3

print(10%3) #Gives remainder 1

#COMPARISION OPERATORS : 
print(True=="True") #Gives False
print(10%2 == 0) 

#LOGICAL OPERATORS :
print(2+1==3 and 1-1==0) 
#BITWISE OPERATORS :
print(10&4) # (00001010) & (00000100) --> 00000000 --> 0
print(10|4) # (00001010) & (00000100) --> 00001110 --> 14
print(~10)  # ~(00001010) --> (11110101) --> -11
#XOR --> ^ --> Gives 1 if both bits are same and 0 if both are different with each other:
print(10^4) # (00001010) | (00000100) --> (00001110) --> 14

#ASSIGNMENT OPERATORS : 
x = 10
x += 1
print(x)
x -= 2
print(x)
x = 10
x *= 3
print(x)


#IDENTITY OPERATORS : 
a = [1,2,3]
b = a
print(a is b) #True
print(b is a) #True
a = [1,2,3]
b = [1,2,3]
print(a is b) #False
print(b is a) #False

#MEMBERSHIP OPERATORS : 
x = 'jeman'
y = {1:'a',2:'b'}
print('j' in x) #True 
print('hello' not in x) #True
print(1 in y) #True
print('a' in y) #False



