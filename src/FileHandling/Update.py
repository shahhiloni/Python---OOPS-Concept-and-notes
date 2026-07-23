## Update File 

import os
FILE_NAME = "hello.txt"

def update_student():

    roll_no = input("Enter Roll Number to Update: ")
    updated_data = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, course, marks = line.strip().split(",")

            if roll == roll_no:
                found = True

                print("\nEnter New Details")
                name = input("New Name: ")
                course = input("New Course: ")
                marks = input("New Marks: ")

            updated_data.append(f"{roll},{name},{course},{marks}\n")
    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_data)
        print("Record Updated Successfully")

    else:
        print("Student Not Found")

update_student()