class Bank: 
    def __init__(self):
        self.name = "hello"
        self.__balance = 1000 

    def show_balance(self):
        print(self.__balance)

obj = Bank()
obj.show_balance()

class Bank: 
    def __init__(self):
        self.name = "hello"
        self.balance = 1000 

    def show_balance(self):
        print(self.balance)

obj = Bank()
obj.show_balance()


class Bank:
    def __init__(self):
        self.__balance = 2000

obj = Bank()
print(obj.__balance)

# // account number 
# // balance