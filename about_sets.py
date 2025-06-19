#A collection which is unordered, Unchangeable (removal and adding allowed) and unindexed.
#No Duplicates allowed. Duplicated will be removed even if included.
#Uses "{}" brackets

a = set()
b = {20}
c = {'a',1,2,3}
d = {1,2,1,1,1,0}
print(d)

#Modifying a set : 
s = {1,2,3,4}
y = {5,6}
x = [45]
z = ('jeman')
a = ('jeman','jack')
s.update(y)#This will change the original 's' set by adding y's 5 and 6 to it
print(s) #{1,2,3,4,5,6}
s.update(x) 
print(s) #{1,2,3,4,5,6,45}
s.update(z)
print(s) #{1,2,3,4,5,6,45,'j','e','m','a','n'}
s.update(a)
print(s) #{1,2,3,4,5,6,45,'j','e','m','a','n','jeman','jack'}
s.add('doe')
print(s) #{1,2,3,4,5,6,45,'j','e','m','a','n','jeman','jack','doe'}

s.clear() #{}

s = {12,15,13,22,16,17}
t = {13,15,22}
print(s.issuperset(t)) #True
print(s.issubset(t))   #False
print(s.isdisjoint(t)) #False

#Math operations:
s = {1,2,3,4,5}
y = {1,3,5,9}
print(s|y) # {1,2,3,4,5}
print(s&y) # {1,3,5}
print(s-y) # {2,4}
print(y-s) # empty set
print(s^y) # result of(s-y) U (y-s) --> {2,4}

d={0,0,0,1,1,1,1,1,2,"jeman","jeevan"}
print(d)
for i in d:
    print(i)

for index,value in enumerate(d):
    print(f'{index}:{value}')

#The following gives error. If you dont' want error convert 'd' to list like this : list(d)
for i in range(len(d)):
    print(d[i])


