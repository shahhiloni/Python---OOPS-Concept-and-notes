# A decorator is a function that adds extra feature or functionality without changing original function 


# step: 1 : original function 

# step: 2: decorator (add extra features)

# step: 3: updated function 


## user authentication 
## logging 
## timing function 
## error handling 

## logging 

is_logged_in = True 

def login_required(func):
    def wrapper(): 
        if is_logged_in:
           func()
        else: 
           print("user should be login first")
    return wrapper 

@login_required
def dashboard():
    print("user navigator to the dashboard")

dashboard()
