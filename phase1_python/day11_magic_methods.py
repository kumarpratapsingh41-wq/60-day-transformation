# Day 11 - Magic Methods

# ===== __str__ AND __repr__ =====
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"      # for end users

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"  # for developers

p = Point(3, 4)
print(p)        # Point(3, 4)
print(repr(p))  # Point(x=3, y=4)

# ===== __len__ AND __eq__ =====
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other.items

c1 = Cart()
c1.add("apple")
c1.add("banana")

c2 = Cart()
c2.add("apple")
c2.add("banana")

print(len(c1))   # 2
print(c1 == c2)  # True — contents are equal

# ===== __add__ — OPERATOR OVERLOADING =====
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v3)       # Vector(4, 6)
print(len(v1))  # 2