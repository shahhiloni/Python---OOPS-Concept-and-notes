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
is_logged_in = False

def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Please Login First")
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()

