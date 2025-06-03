#Unordered, mutable & iterable collection of key-value pairs with unique keys.
#Duplicate values are allowed. Duplicate keys are not allowed. Even if you use duplicate keys. The newest key will overwrite the old key
#Dicts are also called maps.
person = {
    'name' : 'Jack',
    'age'  : 50,
    'name' : 'Jane'
}

print(person)

print(person['age'])

s = {
    "name" : "Jane Doe",
    "age"  : 50,
    "dogs" : ["snoopy",'dude'],
    'address' : {"Street":'11-2','city':'new york'}
}

lst = [12,13,14,15,16]
e   = dict.fromkeys(lst,25)
print(e)

e2  = dict.fromkeys(lst)
print(e2)

courses = {"CS101":"CPP","CS102":"DS","CS201":"OOP","CS226":"DAA","CS601":"CRYPT","CSS42":"Web"}
courses['CS444'] = 'Biology'
courses['CS201'] = 'Java'
print(len(courses))

del(courses['CS102'])
print(courses)
print(len(courses))
courses.clear()
print(courses)
courses.update({"Math":"Algebra","Science":"Material Science"})
print(courses)
print(max(courses))
print("Math" in courses)

#Iterating through dicts : 
person = {
    "name" : "Alice",
    "age"  : 25,
    "city" : "Delhi"
}

for key in person :
    print(key)

for key in person.keys():
    print(f"{key} : -- : {person[key]}")

for val in person.values():
    print(val)

for key, val in person.items():
    print(f"{key} : {val}")

for index,(key,value) in enumerate(person.items()):
    print(index,key,value)

person = {
    "name":"Jeman",
    "age" : 50,
    "legs": 4
}

for key,value in person.items():
    if isinstance(value,int):
        print(f'{key} is numeric')