# Day 7 - Decorators

import time
import functools

# ===== BASIC DECORATOR =====
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

# ===== @decorator is shorthand for =====
# say_hello = my_decorator(say_hello)

# ===== TIMER DECORATOR =====
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

print(slow_function())

# ===== STACKED DECORATORS =====
# Applied bottom up, executed top down
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())  # <b><i>Hello</i></b>

# ===== LOGGER DECORATOR =====
def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 4)

# ===== FUNCTOOLS.WRAPS DIFFERENCE =====
def logger_without(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def logger_with(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@logger_without
def add1(a, b):
    return a + b

@logger_with
def add2(a, b):
    return a + b

print(add1.__name__)  # wrapper
print(add2.__name__)  # add2
print(add.__name__)   # add — functools.wraps preserved the name