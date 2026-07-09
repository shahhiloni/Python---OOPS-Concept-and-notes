# Inheritance : one class acquires the properties and methods of another class.

# Parent Class = SuperClass
# Child Class = SubClass

# // single inheritance : one Parent --> one Child

# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")
        
# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

obj = Dog()

obj.sound()
obj.bark()

# // multiple inheritance : Multiple parent --> One Child

class Father:
    def skills1(self):
        print("Driving")

class Mother:
    def skills2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

obj = Child()

obj.skills1()
obj.skills2()

# # multi - level inheritance : GrandParent --> Parent --> Child

class Animal:
    def eat(self):
        print("Eating")

class Mammal(Animal):
    def walk(self):
        print("Walking")
       
class cat(Mammal):
    def meow(self):
        print("Barking")

class Dog(cat):
    def bark(self):
        print("Barking")

obj = Dog()

obj.eat()
obj.walk()
obj.meow()
obj.bark()

# Hierarchical Inheritance : one parent class --> two or more than child Class
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()

# # Hybrid inheritance : combination of Two or more than two methods
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")

class Puppy(Dog, Cat):
    pass

obj = Puppy()

obj.eat()
obj.bark()
obj.meow()