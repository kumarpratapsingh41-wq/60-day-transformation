# Day 3 - List, Tuple, Set, Dict Internals

import sys

# ===== LIST OPERATIONS COMPLEXITY =====
a = [1, 2, 3]
a.append(4)      # O(1)
a.insert(0, 0)   # O(n) - shifts all elements
a.pop()          # O(1)
a.pop(0)         # O(n) - shifts all elements

# ===== DICT VS LIST LOOKUP =====
d = {"name": "John", "age": 25}
print("name" in d)              # O(1) - hash table
print("name" in ["name", "age"]) # O(n) - traversal

# ===== TUPLE VS LIST MEMORY =====
a = [1, 2, 3]
b = (1, 2, 3)
print(sys.getsizeof(a))  # 80 - over allocated
print(sys.getsizeof(b))  # 64 - exact

# ===== LIST OVER ALLOCATION =====
a = []
for i in range(10):
    a.append(i)
    print(f"Length: {len(a)}, Size: {sys.getsizeof(a)}")

# ===== TUPLE IMMUTABILITY TRAP =====
a = (1, 2, [3, 4])
a[2].append(5)
print(a)  # (1, 2, [3, 4, 5]) - tuple ref unchanged, list mutated

# ===== SET VS LIST MEMBERSHIP =====
data = [1, 2, 3, 4, 5]
data_set = {1, 2, 3, 4, 5}
print(5 in data)      # O(n)
print(5 in data_set)  # O(1)