
class Payment:
    def __init__(self, payment_methods):
        self.payment_methods = payment_methods
    def chose_payment_method(self, method):
     
        if method in self.payment_methods:
            print(f"Choose payment method: {method}")
        else:
            print(f"{method} is not available. Please choose a different payment method.")
    def cancel_payment(self):
        print("Payment transaction cancelled.")


payment = Payment(["credit_card", "paypal", "cash"])

payment.chose_payment_method("credit_card")

payment.cancel_payment()

