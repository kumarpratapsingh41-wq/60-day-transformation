# Day 6 - Iterators and Generators

# ===== ITERATOR PROTOCOL =====
my_list = [1, 2, 3]
print(hasattr(my_list, '__iter__'))  # True
print(hasattr(my_list, '__next__'))  # False

it = iter(my_list)
print(hasattr(it, '__iter__'))  # True
print(hasattr(it, '__next__'))  # True

# ===== HOW FOR LOOP WORKS INTERNALLY =====
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

# ===== CLASS BASED ITERATOR =====
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in CountUp(1, 5):
    print(num)

# ===== GENERATOR WITH YIELD =====
def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

for num in count_up(1, 5):
    print(num)

# ===== YIELD VS RETURN =====
def using_yield():
    yield 1
    yield 2
    yield 3

for val in using_yield():
    print(val)

# ===== PRACTICAL USE - LARGE FILE =====
def read_large_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.strip()
# Only one line in memory at a time — handles files of any size