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
print(f.split('*')) #Gives ['a','b','c','d','e','f']

g = 'jemankumar'
print(g.startswith('je')) #Gives True

h = 'Truethat'
#print(h.startswith(True))#Gives error

print(h.startswith('True')) #Gives True

print(h.endswith('that')) #Gives True

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
print(m.isalnum()) #True alnum means alphas or nums

str = 'Jeman is an idiot'
print('Hello, {}'.format(str))
print(f"Hi {str}")

numr = '42'
print(numr.zfill(4)) #Prints 0042
print(str.zfill(30)) #Prints 0000000000000Jeman is an idiot
print(numr.center(10)) #Creates a string of length 10 and puts '42' in the middle
print(numr.ljust(10)) #
print(numr.rjust(10)) #

for n in 'hello':
    print(n)

if 'a' in 'apple':
    print (True)