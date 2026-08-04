# ## Opening a file  : open() 

# # file = open ("filename.txt", "mode")

# # reading a file : read(), readline(), readlines()

# file = open ("filename.txt", "r")
# print(file.read())
# file.close()

# #writing a file :  write()
# file = open ("filename.txt", "w")
# file.write("hello, Good morning")
# file.close()

# ## appending a file 
# file = open("filename.txt", "a")
# file.write("\n welcome")
# file.close()

# import os 

# if os.path.exists("File_Handling.txt"):
#     print("file exists")
# else: 
#     print("file not found")


# #deleting a file - remove()
# import os 
# os.remove("filename.txt")

# #with statement - using for automatically closing the file 
# with open("filename.txt", "w") as file:
#     file.write("hello, Good morning")


import json

students = {}

# Add Student
def add_student(name, age, course, marks):
    students[name] = {
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# # Display Students
# def display_student():
#     try:
#         with open("students.json", "r") as file:
#             data = json.load(file)
#             print(data)
#     except FileNotFoundError:
#         print("No student records found.")


# Search Student
# def search_student(name):
#     try:
#         with open("students.json", "r") as file:
#             data = json.load(file)

#         if name in data:
#             print(data[name])
#         else:
#             print("Student Not Found")

#     except FileNotFoundError:
#         print("No student records found.")


# Example
add_student("Rahul", 20, "Python", 90)
add_student("Priya", 21, "Java", 85)

# display_student()

# search_student("Rahul")
# search_student("Amit")

