import os
FILE_NAME = "hello.txt"

# Create file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            pass

create_file()

