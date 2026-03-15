# Day 9 - OOP Part 1: Classes, Instance vs Class Variables, Methods

# ===== CUSTOM EXCEPTION =====
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}. Balance is {balance}")

# ===== CLASS VS INSTANCE VARIABLES =====
class Dog:
    species = "Canis familiaris"  # class variable — shared across all instances

    def __init__(self, name, age):
        self.name = name  # instance variable — unique to each object
        self.age = age

d1 = Dog("Rex", 5)
d2 = Dog("Bruno", 3)

print(d1.species)   # Canis familiaris
print(d2.species)   # Canis familiaris
print(d1.name)      # Rex

# Class variable change via class — affects all instances
Dog.species = "Changed"
print(d1.species)   # Changed
print(d2.species)   # Changed

# Instance variable assignment — creates own copy, shadows class variable
d1.species = "Only d1"
print(d1.species)   # Only d1
print(d2.species)   # Changed
print(Dog.species)  # Changed

# ===== BANK ACCOUNT CLASS =====
class BankAccount:
    interest_rate = 0.05  # class variable

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. Balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"{amount} withdrawn. Current balance is {self.balance}")

    def get_balance(self):
        return f"The current balance is {self.balance}"

    @classmethod
    def get_interest_rate(cls):
        return f"The interest rate is {cls.interest_rate}"

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError("Amount cannot be less than or equal to 0")
        return f"Valid amount: {amount}"

# ===== USAGE =====
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())
print(BankAccount.get_interest_rate())
print(BankAccount.validate_amount(100))

try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print(e)

try:
    BankAccount.validate_amount(-50)
except ValueError as e:
    print(e)