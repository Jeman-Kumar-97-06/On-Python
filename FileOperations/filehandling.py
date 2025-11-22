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
f = open('demo.txt') # Same as f = open('demo.txt','rt') --> Open in read mode & text mode.
print(f) #--> Outputs <_io.TextIOWrapper name='demo.txt' mode='r' encoding='UTF-8'>
print(f.read()) #-->Prints the content of txt file.
print(f.closed)
f.close()
print(f.closed)