nums   = [10,5,7,31,2,1]
strs   = ['cats','dogs','jeman','kumar','sai','rani','ravi']
fruits = ['orange','apple','guava','jackfruit','chickoo','banana','mango'] 
nests  = ['jack','jane',['john','doe']]

print(nums[0])    #Gives 10
print(nums[-1])   #Gives 1
print(len(nums))  #Gives 6
print(max(nums))  #Gives 31

print(strs[0],strs[-1]) # Prints cats and ravi
print(strs[2:])         # Prints 'jeman','kumar','sai','rani','ravi'

a,b,c,d,e,f,g = fruits
print(a,b,c)
a,*b,c = fruits
print(b)

*a,[x,y] = nests
print(a)          # Prints "Jack", "Jane"
print(x,y)        # Prints 'john', 'doe'

nums.append('jeevan') # Adds "jeevan" to the end of the nums list
print(nums)
nums.remove(10)       # Removes the value 10 from the list
print(nums)
nums.pop()            # Removes the last element
print(nums)
nums.pop(3)           # Removes the element at index 3
print(nums)
nums.insert(3,'hell') # changes [5,7,31,1] to [5,7,31,'hell',1]
print(nums)
fruits.reverse()      # Reverses the order
print(nums.count(7))  # Prints how many times 7 occured in the list
print(nums.index(31)) # Prints the index of the value 31
nums[1:3] = ["hell",'heaven']
print(nums)

