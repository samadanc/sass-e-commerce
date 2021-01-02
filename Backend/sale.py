import datetime as dt  # This will require us to use datetime python library


# We also need the tkcalendar library on the frontend
# We do not want to install any new library for the project, so you can leave the sales feature out of your project
class Sale:
    def __init__(self, seller, products, discount, from_date, to_date):
        self.seller = seller
        self.products = products  # list of product names
        self.discount = discount  # discount in percentage
        self.from_date = from_date
        self.to_date = to_date

    def __str__(self):
        products_str = str(self.products)
        # Bad Logic: We expect product names to not contain any of these characters
        products_str = products_str.replace(" ", "")
        products_str = products_str.replace("'", "")
        products_str = products_str.replace(",", ";")
        date_format = '%Y%m%d%H%M%S'
        return self.seller + "," + products_str + "," + str(self.discount) + "," + self.from_date.strftime(date_format) + "," + self.to_date.strftime(date_format)

    def __contains__(self, product):
        if product in self.products:
            return True
        else:
            return False

    def get_seller(self):
        return self.seller

    def get_products(self):
        return self.products

    def get_from_date(self):
        return self.from_date

    def get_to_date(self):
        return self.to_date

    def get_discount(self):
        return self.discount

    def set_seller(self, seller):
        self.seller = seller

    def set_products(self, products):
        self.products = products

    def set_discount(self, discount):
        self.discount = discount

    def set_from_date(self, from_date):
        self.from_date = from_date

    def set_to_date(self, to_date):
        self.to_date = to_date
