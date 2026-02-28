# Day 1 - Python Memory Model: Mutable vs Immutable

# ===== IMMUTABLE EXAMPLE =====
x = 10
y = x
y = 20
print(x)  # 10 - x is unchanged because integers are immutable
print(id(x) == id(y))  # False - y points to a new object

# ===== MUTABLE EXAMPLE =====
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] - both a and b point to same object
print(id(a) == id(b))  # True - same object in memory

# ===== MUTABLE DEFAULT ARGUMENT TRAP =====
def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]
print(add_item(3))  # [1, 2, 3]  -- default list is shared!

# ===== THE FIX =====
def add_item_fixed(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(add_item_fixed(1))  # [1]
print(add_item_fixed(2))  # [2]
print(add_item_fixed(3))  # [3]

# ===== STRINGS ARE IMMUTABLE =====
a = "hello"
b = a
b = b + " world"
print(a)  # hello - unchanged
print(id(a) == id(b))  # False - new object created