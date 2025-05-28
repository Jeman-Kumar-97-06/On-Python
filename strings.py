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