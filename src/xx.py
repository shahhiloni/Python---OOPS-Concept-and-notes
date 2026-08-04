class BankAccount:
    def __init__(self, name, acc, balance):
        self.name = "hiloni"
        self.acc = 33333
        self.balance = 10

    def deposit(self, amt):
        if amt > 0:
            self.balance += 2000
            print(f"₹{amt} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= 2000
            print(f"₹{amt} withdrawn successfully.")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)