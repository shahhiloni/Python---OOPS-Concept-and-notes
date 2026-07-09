# from abc import ABC, abstractmethod
# class Parent(ABC):

#     @abstractmethod
#     def display(self):
#         pass 

# class Child(Parent):
       
#       def display(self):
#            print("implement method")

# obj = Child()
# obj.display()


from abc import ABC, abstractmethod
class payment(ABC):
 
      @abstractmethod
      def pay(self):
        pass

class CreditCard(payment):
       
       def pay(self): 
            print("Payment done using Credit Card")

class UPI(payment):
       
       def pay(self): 
            print("Payment done using UPI")

class NetBanking(payment):
       
       def pay(self): 
            print("Payment done NetBanking")

Card = CreditCard()
upi = UPI()
bank = NetBanking()


Card.pay()
upi.pay()
bank.pay()