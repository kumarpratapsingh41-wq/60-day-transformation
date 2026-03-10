# Day 4 - Comprehensions and Generator Expressions

import sys

# ===== LIST COMPREHENSION =====
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# ===== DICT COMPREHENSION =====
names = ["alice", "bob", "charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {"alice": 5, "bob": 3, "charlie": 7}

# ===== NESTED COMPREHENSION =====
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ===== GENERATOR VS LIST MEMORY =====
big_list = [x**2 for x in range(100000)]
big_gen = (x**2 for x in range(100000))
print(sys.getsizeof(big_list))  # ~800KB
print(sys.getsizeof(big_gen))   # 112 bytes

# ===== GENERATOR - NEXT() =====
gen = (x**2 for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# ===== GENERATOR EXHAUSTION =====
gen = (x**2 for x in range(3))
for val in gen:
    print(val)  # 0, 1, 4

for val in gen:
    print(val)  # prints nothing - generator exhausted