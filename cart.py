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


cart1 = Cart()
item_added = cart1.add_item('Apple', 3)
print(item_added)

item_added = cart1.add_item('Banana', 2)
print(item_added)

item_added = cart1.add_item('Apple', 2)
print(item_added)  # Quantity updated
print(cart1.items)
