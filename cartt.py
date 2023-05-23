class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    def Order(self, items):
        total = 0
        for item in items:
            total += item['product'].price * item['quantity']
        print(f"Order Total: Ksh{total}")
class Cart:
    def __init__(self):
        self.items = []
    def add_item(self, product, quantity):
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                return "Quantity updated"
        self.items.append({'product': product, 'quantity': quantity})
    def remove_item(self, product):
        for item in self.items:
            if item['product'] == product:
                self.items.remove(item)
    def empty_cart(self):
        self.items = []
    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            price = product.price
            total_price += price * quantity
        return total_price
cart1 = Cart()
item_added = cart1.add_item(Product('Apple', 10, 'Description1'), 6)
print(item_added)
item_added = cart1.add_item(Product('Banana', 20, 'Description2'), 2)
print(item_added)
item_added = cart1.add_item(Product('Mango', 10, 'Description3'), 2)
print(item_added)
total_price = cart1.calculate_total_price()
print("Cart Total Price:", total_price)
print("Cart Items:")
for item in cart1.items:
    print(f"Product: {item['product'].name}, Quantity: {item['quantity']}")
items = [{'product': Product('Product1', 10, 'Description1'), 'quantity': 2},
         {'product': Product('Product2', 20, 'Description2'), 'quantity': 3},
         {'product': Product('Product3', 50, 'Description3'), 'quantity': 4},
         {'product': Product('Product4', 60, 'Description4'), 'quantity': 7},
         {'product': Product('Product5', 40, 'Description5'), 'quantity': 9}]
order_product = Product('Product6', 30, 'Description6')
order_product.Order(items)