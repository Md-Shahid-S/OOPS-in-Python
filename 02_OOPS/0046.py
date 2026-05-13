''''  
Build a ShoppingCart class that uses all three forms of polymorphism:

Method overriding: Create a base Discount class with an abstract apply(amount) method. 
Then create FlatDiscount(amount) and PercentageDiscount(percent) subclasses — both override apply() differently.

Duck typing: Write a function print_receipt(cart) that calls cart.get_items() and cart.get_total() 
— it should work as long as the object has those methods, no inheritance needed.

Operator overloading: Implement __add__ on ShoppingCart so that cart1 + cart2 merges both carts into a new one, 
and __len__ so len(cart) returns the number of items.

'''
from abc import ABC, abstractmethod

# ---------------------------------------------------------
# 1. Method Overriding (Subtype Polymorphism)
# ---------------------------------------------------------
class Discount(ABC):
    @abstractmethod
    def apply(self, amount: float) -> float: 
        pass       

class FlatDiscount(Discount):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, amount: float) -> float:
        # Subtract flat amount, ensuring total doesn't drop below $0
        return max(0.0, amount - self.amount)

class PercentageDiscount(Discount):
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, amount: float) -> float:
        # Subtract the percentage from the total
        return amount * (1 - (self.percent / 100))


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discounts = []

    def add_item(self, name: str, price: float):
        self.items.append((name, price))

    def add_discount(self, discount: Discount):
        self.discounts.append(discount)

    def get_items(self):
        return self.items

    def get_total(self):
        total = sum(price for _, price in self.items)
        for discount in self.discounts:
            # Polymorphism in action: Python doesn't care if it's a Flat or Percentage discount,
            # it just knows to call apply() and the subclass handles the specific math.
            total = discount.apply(total)
        return max(0.0, total)

    # ---------------------------------------------------------
    # 2. Operator Overloading (Ad-hoc Polymorphism)
    # ---------------------------------------------------------
    def __add__(self, other: "ShoppingCart") -> "ShoppingCart":
        new_cart = ShoppingCart()
        new_cart.items = self.items + other.items
        new_cart.discounts = self.discounts + other.discounts
        return new_cart

    def __len__(self) -> int:
        return len(self.items)


# ---------------------------------------------------------
# 3. Duck Typing
# ---------------------------------------------------------
def print_receipt(cart):
    """
    This function demonstrates Duck Typing. 
    It has no type hints and doesn't explicitly check if 'cart' is a ShoppingCart. 
    As long as the object walks like a duck (has .get_items()) and quacks like a duck 
    (has .get_total()), this function will work.
    """
    print("=== RECEIPT ===")
    for name, price in cart.get_items():
        print(f"{name.ljust(15)} ${price:.2f}")
    
    print("-" * 25)
    print(f"TOTAL:          ${cart.get_total():.2f}")
    print("===============\n")


# =========================================================
# Testing the Implementation
# =========================================================
if __name__ == "__main__":
    # Cart 1 setup
    cart1 = ShoppingCart()
    cart1.add_item("Python Book", 40.0)
    cart1.add_item("Coffee Mug", 15.0)
    cart1.add_discount(PercentageDiscount(10)) # 10% off

    # Cart 2 setup
    cart2 = ShoppingCart()
    cart2.add_item("Mechanical Keyboard", 120.0)
    cart2.add_discount(FlatDiscount(20)) # $20 off

    # Demonstrate Operator Overloading (__add__ and __len__)
    merged_cart = cart1 + cart2
    
    print(f"Items in Cart 1: {len(cart1)}")
    print(f"Items in Cart 2: {len(cart2)}")
    print(f"Items in Merged: {len(merged_cart)}\n")

    # Demonstrate Duck Typing & Method Overriding (calculating discounts seamlessly)
    print("--- Printing Cart 1 ---")
    print_receipt(cart1)

    print("--- Printing Merged Cart ---")
    print_receipt(merged_cart) 
