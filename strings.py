a = "jeman kumar"
a.capitalize() # Returns a capitalized string. It doesn't change the original string
print(a.capitalize()) #Gives 'Jeman kumar' not 'Jeman Kumar'

b = 'JEMAN KUMAR'
print(b.lower())

c = "   Jeman    "
c.strip() 
print(c) # Doesn't change the string.
print(c.strip())


d = 'Jeman Kumar'
print(d.replace('a','b')) #Gives Jembn Kumbr
print(d) #Gives Jeman Kumar

e = ['jeman','jack','john','doe']
print('*'.join(e))

f = 'a*b*c*d*e*f'
print(f.split('*'))

g = 'jemankumar'
print(g.startswith('je'))

h = 'Truethat'
#print(h.startswith(True))#Gives error

print(h.startswith('True'))

print(h.endswith('that'))

i = 'heeeeellllooo'
print(i.find('e')) #Prints index of the first occurence of 'e'

j = 'heelloo'
print(j.count('e')) #2

k = 'h'
print(k.isalpha()) #True

l = '123'
print(l.isdigit()) #True

m = '123n'
print(m.isdigit()) #False