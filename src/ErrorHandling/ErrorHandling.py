# In Python, error handling is done using the try, except, else, and finally blocks. 
# This allows your program to handle runtime errors gracefully instead of crashing.


## basic syntax
try:
    x = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")


## Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Catching Any Exception

try:
    x = int("abc")

except Exception as e:
    print("An error occurred:", e)

# Using else : The else block executes only if no exception occurs.
    
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", num)

# Using finally : The finally block always executes, whether an exception occurs or not.

try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

# Raising Exceptions : You can raise your own exceptions using raise.
    
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")

# Custom Exceptions

class InvalidAgeError(Exception):
    pass

age = -2

if age < 0:
    raise InvalidAgeError("Invalid age entered.")