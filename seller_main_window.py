from tkinter import *


class SellerMainWindow(Tk):
    def __init__(self, username):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - Main")
        self.geometry('500x500')
        self.entries = []
        self.submitted_data = []

    def get_product_frame(self, name, price, seller):
        product_frame = Frame(self)
        Label(product_frame, text="Name: "+name).grid(row=0, column=0)
        Label(product_frame, text=", ").grid(row=0, column=1)
        Label(product_frame, text="Price: "+price).grid(row=0, column=2)
        Label(product_frame, text="Seller: "+seller).grid(row=1, column=2)
        return product_frame
##        self.initialize_labels()
##        self.initialize_entries()
##        self.initialize_button()
        self.fetch_existing_products()

##
##
##    def get_data(self):
##        entries_list = [entry.get() for entry in self.entries]
##        return ",".join(entries_list)
##
##    def initialize_labels(self):
##        Label(self, text='Name').grid(row=0,column=0)
##        Label(self, text='Age').grid(row=1,column=0)
##        Label(self, text='Location').grid(row=2,column=0)
##    def initialize_entries(self):
##        for i in range(3):
##            self.entries.append(Entry(self))
##            self.entries[i].grid(row=i,column=1)
##    def initialize_button(self):
##        b = Button(self, text="Submit", command=self.on_submit_click)
##        b.grid(row=3, column=1)
##    def on_submit_click(self):
##        t = self.get_data()
##        with open(db_file, mode="a") as db:
##            db.write(t + '\n')
##        self.submitted_data.append(t)
##        Label(self, text=t, padx=30).grid(row=len(self.submitted_data)-1, column=2)