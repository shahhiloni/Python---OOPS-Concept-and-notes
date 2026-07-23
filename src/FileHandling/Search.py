## search existing data from file 

import os
FILE_NAME = "students.txt"

def search_student():
    roll_no = input("Enter Roll Number: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, course, marks = line.strip().split(",")

            if roll == roll_no:
                print("\nRecord Found")
                print("Roll :", roll)
                print("Name :", name)
                print("Course :", course)
                print("Marks :", marks)
                found = True
                break

    if not found:
        print("Student Not Found")

search_student()
