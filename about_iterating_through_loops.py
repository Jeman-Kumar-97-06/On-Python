#Using for loop : 
items = ['apple','banana','cherry']
for item in items :
    print(item)

#Using range and indexing:
for i in range(len(items)):
    print(items[i])

#Using enumerate:
for index, value in enumerate(items):
    print(f"{index} : {value}")

#Using a while loop:
i = 0
while i < len(items):
    print(items[i])
    i += 1

#Using a map function:
def func(x):
    print(x)
    return
list(map(func,items))

#Using a zip function:
prices = [10,20,30]
for items,price in zip(items,prices):
    print(f'{item} : {price}')

