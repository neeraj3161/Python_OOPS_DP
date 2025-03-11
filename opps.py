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
