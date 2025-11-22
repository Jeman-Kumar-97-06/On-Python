fruits = ['apple','mange','cherry']
#for LOOP
for f in fruits:
    print(f)

for char in 'hello':
    print(char)

for i in range(5):
    print(i)

#while LOOP
count = 0
while count < 5 : 
    print(count)
    count += 1

#'break' statement to exit loop early:
for i in range(10):
    if i == 5:
        break
    print(i)

#'continue' statement to skip current iteration:
for i in range(10):
    if i == 2:
        continue
    print(i)
    