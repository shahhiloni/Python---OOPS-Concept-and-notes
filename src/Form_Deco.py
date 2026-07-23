def validate_registration(func):

    def wrapper():
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username == "":
            print("Username cannot be empty.")
            return

        if len(password) < 6:
            print("Password must be at least 6 characters.")
            return

        # Pass validated data to the original function
        func(username, password)

    return wrapper

@validate_registration
def register(username, password):
    print("\nRegistration Successful")
    print("Username:", username)
    
register()