## Opening a file  : open() 

# file = open ("filename.txt", "mode")

# reading a file : read(), readline(), readlines()

file = open ("filename.txt", "r")
print(file.read())
file.close()

#writing a file :  write()
file = open ("filename.txt", "w")
file.write("hello, Good morning")
file.close()

## appending a file 
file = open("filename.txt", "a")
file.write("\n welcome")
file.close()

import os 

if os.path.exists("File_Handling.txt"):
    print("file exists")
else: 
    print("file not found")


#deleting a file - remove()

import os 
os.remove("filename.txt")


#with statement - using for automatically closing the file 

with open("filename.txt", "w") as file:
    file.write("hello, Good morning")

