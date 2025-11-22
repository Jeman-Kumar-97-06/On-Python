#A collection which is ordered and unchangeable.
#Uses "()" brackets

a = ()
b = ('a','b','c','d',1,2,3,True)
print(b)
c = 'jk',3,3.14
print(c)

d = (*b,*c)

print(d)

x = ('apple','banana','cherry')

for item in x : 
    print(item)

for index,val in enumerate(x) :
    print(f"{index} : {val}")

i = 0
while i < len(x) :
    print(x[i])
    i += 1

def func(x):
    print(x+'fruit')
    return
tuple(map(func,x))