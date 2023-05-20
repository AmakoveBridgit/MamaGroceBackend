class Product:
    def __init__(self,name,price,description,category):
        self.name=name
        self.price=price
        self.description =description
        self.category = category

    def order(self,items):
        self.items = items
        self.total_price = sum([item['product'].price * item['quantity'] for item in items])
        print(f"Order")
        
    def set_category(self, category):
        self.category = category


items = [{'product': Product('Product1', 10, 'Description1'), 'quantity': 2},
         {'product': Product('Product2', 20, 'Description2'), 'quantity': 3}]

product = Product('Product3', 30, 'Description3')
product.set_category('Category3')
product.order(items)

# >>> from MamaGroceryBackend.product import Product
# >>> order=sum([400*2,300*3])
# >>> order
# 1700
# >>> 

# >>> from MamaGroceryBackend.product import Product
# >>> product1=("mango",233,"it is sweeter")
# >>> product1
# ('mango', 233, 'it is sweeter')
# >>> exit()


        