from tkinter import *
from database import *
from message_window import MessageWindow


class ProductForm(Tk):
    def __init__(self, seller):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - New Product")
        self.geometry('500x500')
        self.seller = seller
        self.entries = []
        self.initialize_labels()
        self.initialize_entries()
        self.initialize_button()

    def initialize_labels(self):
        Label(self, text='Name').grid(row=0, column=0)
        Label(self, text='Price').grid(row=1, column=0)
        Label(self, text='Description').grid(row=2, column=0)

    def initialize_entries(self):
        for i in range(3):
            self.entries.append(Entry(self))
            self.entries[i].grid(row=i, column=1)

    def initialize_button(self):
        b = Button(self, text="Submit", command=self.on_submit_click)
        b.grid(row=3, column=1)

    def on_submit_click(self):
        save_product(Product(self.entries[0].get(), self.entries[1].get(), self.entries[2].get(), self.seller))
        self.destroy()
        MessageWindow("Product Added", warning=False).mainloop()
