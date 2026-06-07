class BankAccount:

    def __init__(self, owner: str, balance: float, account_number: str):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number

    # __repr__ — for DEVELOPERS
    # Goal: unambiguous, complete, ideally reproducible
    # Called by: repr(obj), when object is in a collection, in the REPL
    # Rule: should look like the code that created the object if possible
    def __repr__(self) -> str:
        return (
            f"BankAccount(owner='{self.owner}', "
            f"balance={self.balance}, "
            f"account_number='{self.account_number}')"
        )

    # __str__ — for END USERS
    # Goal: readable, friendly, human-facing
    # Called by: print(obj), str(obj), f-strings
    def __str__(self) -> str:
        return f"Account[{self.account_number}] | {self.owner} | ₹{self.balance:,}"


acc = BankAccount("Affu", 75000, "SBI-004521")

print(acc)          # calls __str__  → Account[SBI-004521] | Affu | ₹75,000
print(repr(acc))    # calls __repr__ → BankAccount(owner='Affu', balance=75000, ...)
print(f"{acc}")     # calls __str__  → Account[SBI-004521] | Affu | ₹75,000

accounts = [acc, BankAccount("Ravi", 50000, "SBI-009876")]
print(accounts)     # calls __repr__ on each item in the list