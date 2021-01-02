from tkinter import *
from database import *


class BuyerMainWindow(Tk):
    def __init__(self, username):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - Main")
        self.geometry('500x500')
        self.entries = []
        self.submitted_data = []
        self.initializeScreen()        
    
    def get_product_frame(self, product, location):
        product_frame = Frame(location)
        Label(product_frame, text="Name: "+product.get_name()).grid(row=0, column=0)
        Label(product_frame, text="Price: "+str(product.get_price())).grid(row=1, column=0)
        Label(product_frame, text="Description: "+product.get_description()).grid(row=2, column=0)
        Label(product_frame, text="Seller: "+product.get_seller()).grid(row=3, column=0)
        Button(product_frame, text="Buy", command=self.buy_command).grid(row=4, column=0)
        
        return product_frame

    def product(self, products, frame, index, loc):
        if index < len(products):
            return self.get_product_frame(products[index],frame).grid(row=loc[0], column=loc[1])
        
    def create_multi_frame(self, products):
        multi_frame = Frame(self)
        row = 0
        for i in range(0,len(products),3):
            self.product(products,multi_frame,i,[row,0])
            self.product(products,multi_frame,i+1,[row,1])
            self.product(products,multi_frame,i+2,[row,2])
            row += 1
        return multi_frame
        
    def initializeScreen(self):        
        products = get_products()
        #apply_discounts(products)
        self.create_multi_frame(products).grid(row=0, column=0)

    def buy_command(self):
        print("product bought")