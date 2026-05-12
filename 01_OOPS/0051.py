'''

Build an Invoice class for a freelance billing system:

Instance variables: client_name, amount, currency (default "INR")
Class variable: invoice_count that tracks how many invoices have been created
An instance method apply_gst(rate=18) that adds GST to the amount and returns the final total
A @classmethod called from_string that takes a string like "TechStartup|50000|USD" and creates an Invoice object from it
A @staticmethod called is_valid_amount(amount) that returns True only if the amount is greater than zero
A @classmethod called get_invoice_count() that returns how many invoices have been raised so far

Test all four types of functionality with at least two invoice objects.

'''

class Invoice:
    invoice_count = 0

    def __init__(self, client_name, amount, currency="INR"):
        self.client_name = client_name
        self.amount = amount
        self.currency = currency
        Invoice.invoice_count += 1

    def apply_gst(self, rate=18):
        gst_amount = self.amount * (rate / 100)
        total_amount = self.amount + gst_amount
        return total_amount
    
    @classmethod
    def from_string(cls, invoice_str):
        client_name, amount, currency = invoice_str.split('|')
        return cls(client_name, float(amount), currency)
    
    @staticmethod    
    def is_valid_amount(amount):
        return amount > 0

    @classmethod
    def get_invoice_count(cls):
        return cls.invoice_count
    
# Testing the Invoice class
invoice1 = Invoice("TechStartup", 50000, "USD")
invoice2 = Invoice.from_string("DesignAgency|30000|EUR")

print(f"Invoice 1: Client={invoice1.client_name}, Amount={invoice1.amount} {invoice1.currency}, Total with GST={invoice1.apply_gst()}")
print(f"Invoice 2: Client={invoice2.client_name}, Amount={invoice2.amount} {invoice2.currency}, Total with GST={invoice2.apply_gst()}")
print(f"Total invoices created: {Invoice.get_invoice_count()}") 

# Testing the static method
print(f"Is the amount for invoice 1 valid? {Invoice.is_valid_amount(invoice1.amount)}")
print(f"Is the amount for invoice 2 valid? {Invoice.is_valid_amount(invoice2.amount)}")

