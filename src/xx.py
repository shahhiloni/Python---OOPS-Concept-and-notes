# class BankAccount:
#     def __init__(self, name, acc, balance):
#         self.name = name
#         self.acc = acc
#         self.balance = balance

#     def deposit(self, amt):
#         if amt > 0:
#             self.balance += amt
#             print(f"₹{amt} deposited successfully.")
#         else:
#             print("Invalid deposit amount.")

#     def withdraw(self, amt):
#         if amt > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amt
#             print(f"₹{amt} withdrawn successfully.")

#     def check_balance(self):
#         print(f"Account Holder : {self.name}")
#         print(f"Account Number : {self.acc}")
#         print(f"Current Balance: ₹{self.balance}")

# account = BankAccount("Hiloni", 33333, 10000)

# print("Initial Account Details")
# account.check_balance()

# print("\nDeposit Transaction")
# account.deposit(2000)
# account.check_balance()

# print("\nWithdraw Transaction")
# account.withdraw(1500)
# account.check_balance()


class Employee:
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

full_time = FullTimeEmployee(50000)
part_time = PartTimeEmployee(8, 500)


print("Full-Time Employee Salary: ₹", full_time.calculate_salary())
print("Part-Time Employee Salary: ₹", part_time.calculate_salary())