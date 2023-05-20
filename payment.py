
class Payment:
    def __init__(self, payment_methods):
        self.payment_methods = payment_methods
    def choose_payment_method(self):
        print("Available payment methods:")
        for method in self.payment_methods:
            print(method)
        method = input("Enter payment method: ")
        if method in self.payment_methods:
            print(f"Chosen payment method: {method}")
        else:
            print("Error: Invalid payment method.")
    def cancel_payment(self):
        print("Payment transaction cancelled.")
payment = Payment(["credit_card", "paypal", "cash"])

payment.choose_payment_method()

payment.cancel_payment()








