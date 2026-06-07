class ShoppingCart:

    def __init__(self, owner: str):
        self.owner = owner
        self._items = []   # list of dicts: {name, price, qty}

    def add_item(self, name: str, price: float, qty: int = 1):
        self._items.append({"name": name, "price": price, "qty": qty})
        return self   # enables method chaining: cart.add_item(...).add_item(...)

    def get_total(self) -> float:
        return sum(item["price"] * item["qty"] for item in self._items)

    # len(cart) — how many line items
    def __len__(self) -> int:
        return len(self._items)

    # bool(cart) — is the cart non-empty?
    # Also used by: if cart: ...
    def __bool__(self) -> bool:
        return len(self._items) > 0

    # cart[0] — access items by index
    def __getitem__(self, index: int) -> dict:
        return self._items[index]

    # item in cart — membership check
    def __contains__(self, item_name: str) -> bool:
        return any(item["name"] == item_name for item in self._items)

    # cart1 + cart2 — merge two carts
    def __add__(self, other: "ShoppingCart") -> "ShoppingCart":
        merged = ShoppingCart(f"{self.owner}+{other.owner}")
        merged._items = self._items + other._items
        return merged

    # for item in cart — iteration
    def __iter__(self):
        return iter(self._items)

    def __repr__(self) -> str:
        return f"ShoppingCart(owner='{self.owner}', items={len(self)})"

    def __str__(self) -> str:
        if not self._items:
            return f"{self.owner}'s cart is empty"
        lines = [f"  - {i['name']} x{i['qty']} @ ₹{i['price']}" for i in self._items]
        return f"{self.owner}'s Cart:\n" + "\n".join(lines) + f"\n  Total: ₹{self.get_total():,}"


# Method chaining works because add_item returns self
cart1 = ShoppingCart("Affu")
cart1.add_item("Laptop", 65000).add_item("Mouse", 1500, 2).add_item("USB Hub", 2000)

cart2 = ShoppingCart("Ravi")
cart2.add_item("Monitor", 18000).add_item("Keyboard", 3500)

print(cart1)              # calls __str__
print(f"\n{len(cart1)} items in cart")     # calls __len__
print(f"Cart non-empty: {bool(cart1)}")    # calls __bool__
print(f"Has Laptop: {'Laptop' in cart1}")  # calls __contains__
print(f"First item: {cart1[0]}")           # calls __getitem__

# Iteration — calls __iter__
for item in cart1:
    print(f"  {item['name']}: ₹{item['price'] * item['qty']}")

# Merging — calls __add__
combined = cart1 + cart2
print(f"\nCombined: {combined}")           # calls __str__