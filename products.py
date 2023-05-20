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

items = [{'product': Product('Product1', 10, 'Description1'), 'quantity': 2},
         {'product': Product('Product2', 20, 'Description2'), 'quantity': 3},
         {'product': Product('Product3', 50, 'Description3'), 'quantity': 4},
         {'product': Product('Product4', 60, 'Description4'), 'quantity': 7},
         {'product': Product('Product5', 40, 'Description5'), 'quantity': 9}]

product = Product('Product6', 30, 'Description6')
product.Order(items)


# >>> from MamaGroceBackend.product import Product
# >>> order=sum([400*2,300*3])
# >>> order
# 1700
# >>> 

# >>> from MamaGroceBackend.product import Product
# >>> product1=("mango",233,"it is sweeter")
# >>> product1
# ('mango', 233, 'it is sweeter')
# >>> exit()


        