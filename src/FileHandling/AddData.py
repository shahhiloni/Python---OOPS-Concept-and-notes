## INSERT data in file 

import os
FILE_NAME = "hello.txt"

def add_student():
    print("\n----- Add Student -----")

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{course},{marks}\n")

    print("Student Added Successfully.\n")


add_student()