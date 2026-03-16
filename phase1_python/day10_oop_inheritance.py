# Day 10 - OOP Part 2: Inheritance and Polymorphism

# ===== BASIC INHERITANCE =====
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # parent sets name and age
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def info(self):
        return f"{self.name}, {self.age} years old, {self.breed}"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# ===== POLYMORPHISM =====
animals = [Dog("Rex", 5, "Labrador"), Cat("Whiskers", 3), Dog("Bruno", 2, "Poodle")]
for animal in animals:
    print(animal.speak())  # dynamic dispatch — right method called at runtime

# ===== METHOD OVERRIDING + DYNAMIC DISPATCH =====
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"I am a shape with area {self.area()}"  # calls child's area()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print(Circle(5).describe())
print(Rectangle(4, 6).describe())

# ===== MULTIPLE INHERITANCE =====
class Flyable:
    def fly(self):
        return "I can fly"

class Swimmable:
    def swim(self):
        return "I can swim"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name}: {self.fly()} and {self.swim()}"

d = Duck("Donald")
print(d.describe())

# ===== METHOD RESOLUTION ORDER =====
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "Hello from B"

class C(A):
    def hello(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.hello())       # Hello from B — left to right
print(D.__mro__)       # D → B → C → A → object