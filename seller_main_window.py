from tkinter import *
from database import *
from product_form_window import ProductForm
from sale_form_window import SaleForm


class SellerMainWindow(Tk):
    def __init__(self, username):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - Main")
        self.geometry('500x500')
        self.username = username
        self.entries = []
        self.initialize_menu(username)
        self.initialize_screen(username)
        # self.initialize_labels()
        # self.initialize_entries()
        # self.initialize_buttons()
        # self.fetch_existing_products()

    def initialize_menu(self, username):
        menubar = Menu(self)
        account_menu = Menu(menubar, tearoff=0)
        account_menu.add_command(label=username)
        account_menu.add_separator()
        account_menu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="My Account", menu=account_menu)
        self.config(menu=menubar)

    def get_product_frame(self, product, location):
        product_frame = Frame(location)
        Label(product_frame, text="Name: "+product.get_name()).grid(row=0, column=0)
        Label(product_frame, text="Price: "+str(round(product.get_price(), 2))).grid(row=1, column=0)
        Label(product_frame, text="Seller: "+product.get_seller()).grid(row=2, column=0)
        return product_frame
    
    def get_sale_frame(self, sale, location):
        sale_frame = Frame(location)
        Label(sale_frame, text="From "+str(sale.get_from_date())+", To "+str(sale.get_to_date())).grid(row=0, column=0)
        Label(sale_frame, text="Products: "+str(sale.get_products())).grid(row=1, column=0)
        Label(sale_frame, text="Discount: "+str(sale.get_discount())).grid(row=2, column=0)
        return sale_frame

    def create_multi_frame(self, data, command):
        multi_frame = Frame(self)
        current_row = 0
        for item in data:
            command(item, multi_frame).grid(row=current_row, column=0)
            current_row += 1
        return multi_frame
    
    def initialize_screen(self, username):
        Button(self, text="Add Product", command=self.add_product).grid(row=0, column=0)
        Button(self, text="Start Sale", command=self.start_sale).grid(row=0, column=1)
        
        Label(self, text="").grid(row=1, column=0)
        Label(self, text="Current Products: ").grid(row=2, column=0)
        
        products = get_seller_products_with_discount(username)
        self.create_multi_frame(products, self.get_product_frame).grid(row=3, column=0)
    
        
        Label(self, text="").grid(row=1, column=1)
        Label(self, text="Current Sales: ").grid(row=2, column=1)

        sales = get_sales()
        self.create_multi_frame(sales, self.get_sale_frame).grid(row=3, column=1)

    def add_product(self):
        ProductForm(self.username).mainloop()

    def start_sale(self):
        SaleForm(self.username).mainloop()
