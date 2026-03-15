# Day 8 - Exception Handling

# ===== BASIC TRY/EXCEPT/FINALLY =====
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")

# ===== MULTIPLE EXCEPTIONS =====
def parse_input(value):
    try:
        result = 10 / int(value)
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input — not a number")
    finally:
        print("Cleanup done")

parse_input("0")
parse_input("abc")
print(parse_input("2"))

# ===== ELSE BLOCK =====
# else runs only when no exception was raised
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result is {result}")
    finally:
        print("Cleanup done")

divide(10, 2)
divide(10, 0)

# ===== RAISING EXCEPTIONS =====
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unrealistically high")
    return f"Valid age: {age}"

try:
    print(validate_age(-5))
except ValueError as e:
    print(f"Validation error: {e}")

# ===== CUSTOM EXCEPTIONS =====
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    result = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)