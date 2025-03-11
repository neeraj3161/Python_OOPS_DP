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

