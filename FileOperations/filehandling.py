"""
Opening a file needs 'open' function.
 Open function takes 2 parameters: filename and mode.
 mode : 
   'r' : Read --> Opens a file for reading, does not create file if it doesn't exists. Just gives error.
   'a' : Append --> Opens a file for appending, creates if the files doesn't exist.
   'w' : Write --> Opens file for writing. creates the file if it doesn't exist.
   'x' : Create --> Creates the specified file, returns an error if the file exists.
 additional mode to add the the mode :
    't' : Text mode.
    'b' : Binary Mode.
""" 
import os
f = open('demo.txt') # Same as f = open('demo.txt','rt') --> Open in read mode & text mode.
print(f) #--> Outputs <_io.TextIOWrapper name='demo.txt' mode='r' encoding='UTF-8'>
print(f.read()) #-->Prints the content of txt file.
print(f.closed)
f.close()
print(f.closed)

#If you don't want to manually close the file :
with open('demo2.txt') as demo2:
    print(demo2.read())

print(demo2.closed)

with open('demo2.txt') as demo2:
    print(demo2.read(5)) #Read the first 5 chars

with open('demo2.txt') as demo2:
    print(demo2.readline()) #Read & Print the first line.
    print(demo2.readline()) #Read & Print the second line.

with open('demo2.txt') as demo2:
    for x in demo2:
        print(x) #Prints all lines

#appends data to 'demo3'
with open('demo3.txt','a') as demo3:
    f.write('Hello! Welcome to "demo3.txt"')

#deletes everything and write shit again:
with open("demo3.txt",'w') as demo3:
    f.write("This is the new content of 'demo3.txt'")

fx = open('myfile.txt','x') #Created an empty file 'myfile.txt'

#Delete a file :
import os
os.remove('filename.txt')

#Check if a file exists and then delete : 
if os.path.exists("filename2.txt"):
    os.remove('filename2.txt')
else:
    print("File does not exist!")

#Delete a folder:
os.rmdir("foldername")