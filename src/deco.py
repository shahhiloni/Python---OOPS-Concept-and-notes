## A Decorator is a function that adds extra functionality to another function without changing its original code.

# Original Function
#         │
#         ▼
# Decorator
# (Add Extra Features)
#         │
#         ▼
# Modified Function

# Suppose every function in your application needs:

# User Authentication
# Logging
# Timing
# Error Handling


def my_decorator(func):

    def wrapper():
        print("Before Function")

        func()

        print("After Function")

    return wrapper

@my_decorator
def greet():
    print("Hello Students")


greet()

# greet() is the original function.
# @my_decorator wraps the greet() function.
# Before greet() executes, "Before Function" is printed.
# After greet() finishes, "After Function" is printed.