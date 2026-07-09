class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):   #Overriding the parent class and method 
        print("Dog barks")

obj = Dog()
obj.sound()