# Day 2 - References & Copying

import copy

# ===== ASSIGNMENT - SAME OBJECT =====
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] - same object
print(id(a) == id(b))  # True

# ===== SHALLOW COPY =====
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]] - inner shared
print(id(a) == id(b))        # False - outer is new
print(id(a[0]) == id(b[0]))  # True - inner is shared

# ===== DEEP COPY =====
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)  # [[1, 2], [3, 4]] - fully independent
print(id(a[0]) == id(b[0]))  # False - inner is new

# ===== FLAT LIST SHALLOW COPY =====
a = [1, 2, 3]
b = copy.copy(a)
b.append(99)
print(a)  # [1, 2, 3] - unaffected