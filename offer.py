class Items:
    def __init__(self, item_name, price, items_on_offer):
        self.item_name = item_name
        self.price = price
        self.items_on_offer = items_on_offer
        self.add_to_cart = {}

    def check_offers_available(self):
        if self.item_name in self.items_on_offer.keys():
            self.add_to_cart[self.item_name] = self.p
        return self.add_to_cart

pineapples = Items("Pineapples", 200, {"Apples": 300, "Mangoes": 200 ,"Pineapples": 200})

mangoes = Items("Mangoes", 500,{ "Apples": 300, "Pineapples": 200, "Mangoes":200})

apples = Items("Oranges", 300, {"Pineapples": 200, "Mangoes": 200, "Apples": 250})


print(pineapples.check_offers_available())

print(mangoes.check_offers_available())

print(apples.check_offers_available())


# {'Pineapples': 200}
# {'Mangoes': 500}
# {"apples":300}


