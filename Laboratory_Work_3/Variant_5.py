class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}"

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Vector({self.x},{self.y})"

class EnhancedList(list):
    def sum(self):
        return sum(self)
    def average(self):
        return self.sum() / len(self) if self else 0
    def unique(self):
        return list(set(self))

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value