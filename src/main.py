import os
FILE_NAME = "students.txt"

# Create file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass

# Add Student
def add_student():
    print("\n----- Add Student -----")

    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{course},{marks}\n")

    print("Student Added Successfully.\n")

# Display Students
def display_students():

    print("\n----- Student Records -----")

    with open(FILE_NAME, "r") as file:

        data = file.readlines()

        if len(data) == 0:
            print("No Records Found\n")
            return

        for line in data:

            roll, name, course, marks = line.strip().split(",")

            print("-------------------------------")
            print("Roll   :", roll)
            print("Name   :", name)
            print("Course :", course)
            print("Marks  :", marks)

    print("-------------------------------")

# Search Student
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

# Update Student
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

# Delete Student
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

# Main Menu
def menu():
    create_file()
    while True:

        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Choice: ")

        try:

            if choice == "1":
                add_student()

            elif choice == "2":
                display_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_student()

            elif choice == "5":
                delete_student()

            elif choice == "6":
                print("Thank You!")
                break

            else:
                print("Invalid Choice")

        except Exception as e:
            print("Error:", e)

menu()