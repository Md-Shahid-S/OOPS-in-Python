class BankAccount:
    """
    A class representing a real bank account.
    The class = the concept of 'what a bank account is'.
    Each object = one specific customer's account.
    """

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


# Creating objects (instances) from the class
account1 = BankAccount()
account1.balance = 5000  # setting state directly (not ideal — we'll fix this with __init__ next)

account2 = BankAccount()
account2.balance = 12000

# Each object is independent
account1.deposit(1000)
print(account1.get_balance())  # 6000
print(account2.get_balance())  # 12000 — untouched

# Checking identity
print(type(account1))           # <class '__main__.BankAccount'>
print(isinstance(account1, BankAccount))  # True