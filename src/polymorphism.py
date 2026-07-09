# // polymorphism : same method with different behaviour

class CreditCard: 
    def pay(self):
        print("Payment done using Credit Card")

class UPI:
    def pay(self):
        print("Payment done using UPI")

class NetBanking:
    def pay(self):
        print("payment done using Netbanking")

payments = [CreditCard(), UPI(), NetBanking()]

for payment in payments:
    payment.pay()


# // payment: upi, creditcard, netbanking
    # // loop : one by one print 

# // payments : store the value or output