class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def say(self):
        print(self.sound)
    
    def __str__(self):
        return f"{self.name} is a {self.color} {self.__class__.__name__}"

class Sheep(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.sound = "Baa, baaaa"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.sound = "Meoooww"

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.sound = "Vav, vavvv"

d = Dog("Reks", "black")
d.say()
print(d)