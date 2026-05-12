from abc import ABC, abstractmethod


# ABC = Abstract Base Class
# Any class that inherits from ABC can have abstract methods
class PaymentMethod(ABC):
    """
    This is the CONTRACT.
    Any class that claims to be a PaymentMethod MUST implement
    process_payment() and refund(). No exceptions.
    """

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.transaction_history = []

    # @abstractmethod means: "I am declaring this method exists,
    # but I refuse to implement it here. Every subclass MUST implement it."
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment. Must return True if successful, False otherwise."""
        pass

    @abstractmethod
    def refund(self, amount: float) -> bool:
        """Refund a payment. Must return True if successful."""
        pass

    # This is a CONCRETE method — implemented here, inherited by all subclasses
    # Subclasses get this for free without reimplementing it
    def get_transaction_count(self):
        return len(self.transaction_history)

    def print_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
            return
        print(f"\nTransaction history for {self.owner_name}:")
        for txn in self.transaction_history:
            print(f"  {txn}")


# ── Concrete class 1 — UPI ──
class UPIPayment(PaymentMethod):

    def __init__(self, owner_name: str, upi_id: str):
        super().__init__(owner_name)   # Call parent __init__ first
        self.upi_id = upi_id

    # MUST implement this — contract fulfilled
    def process_payment(self, amount: float) -> bool:
        if amount <= 0:
            return False
        # In reality this would hit a UPI gateway API
        print(f"[UPI] Sending ₹{amount:,} from {self.upi_id}...")
        print(f"[UPI] Payment of ₹{amount:,} successful!")
        self.transaction_history.append(f"PAID ₹{amount:,} via UPI ({self.upi_id})")
        return True

    # MUST implement this — contract fulfilled
    def refund(self, amount: float) -> bool:
        print(f"[UPI] Refunding ₹{amount:,} to {self.upi_id}...")
        self.transaction_history.append(f"REFUND ₹{amount:,} via UPI")
        return True


# ── Concrete class 2 — Credit Card ──
class CreditCardPayment(PaymentMethod):

    def __init__(self, owner_name: str, card_number: str, credit_limit: float):
        super().__init__(owner_name)
        self.__card_number = card_number   # Encapsulation + Abstraction working together
        self.credit_limit = credit_limit
        self.__used_credit = 0.0

    def process_payment(self, amount: float) -> bool:
        if amount > (self.credit_limit - self.__used_credit):
            print(f"[Card] Payment declined — insufficient credit limit!")
            return False
        # Complex card validation, fraud detection, bank API calls etc.
        # All hidden from the caller
        print(f"[Card] Charging ₹{amount:,} to card ending {self.__card_number[-4:]}...")
        print(f"[Card] Payment of ₹{amount:,} approved!")
        self.__used_credit += amount
        self.transaction_history.append(f"PAID ₹{amount:,} via Card ****{self.__card_number[-4:]}")
        return True

    def refund(self, amount: float) -> bool:
        self.__used_credit -= amount
        print(f"[Card] Refund of ₹{amount:,} posted to card.")
        self.transaction_history.append(f"REFUND ₹{amount:,} to Card")
        return True

    @property
    def available_credit(self):
        return self.credit_limit - self.__used_credit


# ── Concrete class 3 — Wallet ──
class WalletPayment(PaymentMethod):

    def __init__(self, owner_name: str, balance: float):
        super().__init__(owner_name)
        self.__balance = balance

    def process_payment(self, amount: float) -> bool:
        if amount > self.__balance:
            print(f"[Wallet] Insufficient balance! Available: ₹{self.__balance:,}")
            return False
        self.__balance -= amount
        print(f"[Wallet] ₹{amount:,} deducted. Remaining balance: ₹{self.__balance:,}")
        self.transaction_history.append(f"PAID ₹{amount:,} via Wallet")
        return True

    def refund(self, amount: float) -> bool:
        self.__balance += amount
        print(f"[Wallet] ₹{amount:,} refunded to wallet.")
        self.transaction_history.append(f"REFUND ₹{amount:,} to Wallet")
        return True


# ── The power of abstraction — Flipkart's checkout system ──
class CheckoutSystem:
    """
    This class doesn't know or care which payment method is used.
    It only knows that every payment method has process_payment() and refund().
    This is coding against an abstraction, not a concrete implementation.
    """

    def checkout(self, payment: PaymentMethod, amount: float):
        print(f"\n{'='*45}")
        print(f"Processing order for {payment.owner_name} — ₹{amount:,}")
        success = payment.process_payment(amount)
        if success:
            print(f"Order confirmed! Total transactions: {payment.get_transaction_count()}")
        else:
            print("Order failed. Please try a different payment method.")
        print(f"{'='*45}")


# Testing everything together
upi = UPIPayment("Affu", "affu@okaxis")
card = CreditCardPayment("Affu", "4111111111111234", 100_000)
wallet = WalletPayment("Affu", 5000)

checkout = CheckoutSystem()

checkout.checkout(upi, 15000)
checkout.checkout(card, 45000)
checkout.checkout(wallet, 3000)
checkout.checkout(wallet, 3000)   # Should fail — insufficient balance

upi.print_history()
card.print_history()

print(f"\nCard available credit: ₹{card.available_credit:,}")