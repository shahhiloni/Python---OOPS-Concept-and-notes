# In Python, error handling is done using the try, except, else, and finally blocks. 
# This allows your program to handle runtime errors gracefully instead of crashing.


## basic syntax
try:
    # Code that may cause an error
    x = 10 / 0

except ZeroDivisionError:
    # Code to handle the error
    print("Cannot divide by zero.")



