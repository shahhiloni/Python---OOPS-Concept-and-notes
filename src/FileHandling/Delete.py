## delete particular data or entire file 

import os
FILE_NAME = "hello.txt"


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")
    new_data = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, course, marks = line.strip().split(",")

            if roll != roll_no:
                new_data.append(line)

            else:
                found = True
    if found:

        with open(FILE_NAME, "w") as file:
            file.writelines(new_data)

        print("Record Deleted Successfully")

    else:
        print("Student Not Found")

os.remove("hello.txt")
delete_student()