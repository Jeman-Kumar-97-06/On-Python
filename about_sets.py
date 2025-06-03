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