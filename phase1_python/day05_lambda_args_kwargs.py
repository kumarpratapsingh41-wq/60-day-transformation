# Day 5 - Lambda, *args, **kwargs

# ===== LAMBDA =====
square = lambda x: x**2
print(square(5))  # 25

multiply = lambda x, y: x * y
print(multiply(3, 4))  # 12

# ===== LAMBDA WITH SORTED =====
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]
sorted_students = sorted(students, key=lambda s: s["grade"])
print(sorted_students)

# sort descending
sorted_desc = sorted(students, key=lambda s: -s["grade"])
print(sorted_desc)

# ===== *ARGS =====
def add(*args):
    print(type(args))  # tuple
    print(args)
    return sum(args)

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))

# ===== **KWARGS =====
def display(**kwargs):
    print(type(kwargs))  # dict
    print(kwargs)

display(name="Alice", age=25, city="London")

# ===== COMBINING BOTH =====
def mixed(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

mixed(1, 2, 3, 4, 5, name="Alice", age=25)