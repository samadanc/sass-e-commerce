from tkinter import *
from database import *
from datetime import datetime


class SaleForm(Tk):
    def __init__(self, seller):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - New Sale")
        self.geometry('500x500')
        self.seller = seller
        self.entries = []
        self.products = []
        self.chosen_products = []
        self.initialize_products()
        self.initialize_labels()
        self.initialize_entries()
        self.initialize_checkboxes()
        self.initialize_button()

    def initialize_products(self):
        for product in get_seller_products(self.seller):
            self.products.append(product.get_name())

    def initialize_labels(self):
        Label(self, text='Discount').grid(row=0, column=0)
        Label(self, text='From Date (YYYY-MM-DD)').grid(row=1, column=0)
        Label(self, text='To Date (YYYY-MM-DD)').grid(row=2, column=0)

    def initialize_entries(self):
        for i in range(3):
            self.entries.append(Entry(self))
            self.entries[i].grid(row=i, column=1)

    def initialize_checkboxes(self):
        for i in range(len(self.products)):
            var = BooleanVar()
            Checkbutton(self, text=self.products[i], var=var).grid(row=i, column=2)
            self.chosen_products.append(var)

    def initialize_button(self):
        b = Button(self, text="Submit", command=self.on_submit_click)
        b.grid(row=3, column=1)

    def on_submit_click(self):
        from_date = datetime.strptime(self.entries[1], '%Y-%m-%d')
        to_date = datetime.strptime(self.entries[2], '%Y-%m-%d')
        products = []
        for i in range(len(self.chosen_products)):
            if self.chosen_products[i]:
                products.append(self.products[i])
        save_sale(Sale(self.seller, products, self.entries[0], from_date, to_date))
        self.destroy()
