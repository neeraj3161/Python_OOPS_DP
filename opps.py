# classes

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print('Animal make a sound')


Animal('Tiger')

# inheritance

class Dog(Animal):
    def speak(self):
        print(f'{self.name} barks')

# Dog is inheriting animal class
dog = Dog("Dog")
dog.speak()

animal  = Animal("Dog")
animal.speak()  

# multi inheritance

class Parent1:
    def method1(self):
        print(f'Method 1 from parent 1')

class Parent2(Parent1):
    def method2(self):
        print('Method 2 from parent 2')

class Parent3(Parent2):
    def method3(self):
        print('Method 3 from parent 3')


Parent3= Parent3()
Parent3.method1()
Parent3.method2()
Parent3.method3()


# encapsulation
# creating private methods for security to avoid overwriting data
# python creates private method using __variableName
#private attrbutes with getters and setters


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
bnkAcc = BankAccount(1000)
bnkAcc.deposit(5000)
print(bnkAcc.get_balance())


# polymorphism
# same method in multiple classes

class Bird:
    def sound(self):
        print('Bird sound')

class Sparrow:
    def sound(self):
        print('Sparrow sound')

class Crow(Bird):
    def sound(self):
        print("Crow caws")

for obj in [Bird(), Sparrow(), Crow()]:
    obj.sound()

# abstraction

from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Car(vehicle):
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(vehicle):
    def fuel_type(self):
        return "Electric"

car = Car()
ev = ElectricCar()

# Real world example

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  # Calling parent constructor with super and __init__
        self.team_size = team_size

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}")

# Creating objects
emp = Employee("John", 50000)
mgr = Manager("Alice", 80000, 10)

emp.show_details()  # Output: Name: John, Salary: 50000
mgr.show_details()  # Output: Name: Alice, Salary: 80000, Team Size: 10
