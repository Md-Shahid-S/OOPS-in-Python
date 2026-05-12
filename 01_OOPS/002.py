class BankAccount:
    """
    A realistic bank account with proper initialization.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        # These lines run automatically the moment an object is created.
        # 'self.owner' means "this object's owner attribute"
        self.owner = owner
        self.balance = initial_balance
        self.transaction_count = 0
        print(f"Account created for {self.owner} with balance ₹{self.balance}")

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transaction_count += 1
        return self.balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_count += 1
        return self.balance

    def get_summary(self):
        return (
            f"Owner: {self.owner} | "
            f"Balance: ₹{self.balance} | "
            f"Transactions: {self.transaction_count}"
        )


# __init__ fires automatically here — no manual setup needed
account1 = BankAccount("Alice", 10000)   # prints: Account created for Alice...
account2 = BankAccount("Bob")            # uses default balance of 0.0

account1.deposit(2000)
account1.withdraw(500)

print(account1.get_summary())
# Owner: Alice | Balance: ₹11500 | Transactions: 2

print(account2.get_summary())
# Owner: Bob | Balance: ₹0.0 | Transactions: 0