class Product:
    def __init__(self, name, price, description, seller):
        self.name = name
        self.price = price
        self.description = description
        self.seller = seller

    def __str__(self):
        return self.name + str(self.price) + self.description + self.seller

    def __eq__(self, product2):
        return self.name == product2.get_name()

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def get_seller(self):
        return self.seller

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_description(self, description):
        self.description = description

    def set_seller(self, seller):
        self.seller = seller
