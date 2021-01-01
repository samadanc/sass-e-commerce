from tkinter import *
from signup_window import SignupWindow
from message_window import MessageWindow
from seller_main_window import SellerMainWindow
from buyer_main_window import BuyerMainWindow
from database import *


class LoginWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - Login")
        self.geometry('500x500')
        self.entries = []
        self.initialize_labels()
        self.initialize_entries()
        self.initialize_buttons()
        self.seller_checkbox = IntVar()
        Checkbutton(self, text="I am a seller", variable=self.seller_checkbox).grid(row=2, column=1)
    
    def initialize_labels(self):
        Label(self, text='Username').grid(row=0, column=0)
        Label(self, text='Password').grid(row=1, column=0)

    def initialize_entries(self):
        for i in range(2):
            self.entries.append(Entry(self))
            self.entries[i].grid(row=i, column=1)

    def initialize_buttons(self):
        Button(self, text="Sign Up", command=self.on_signup_click).grid(row=3, column=0)
        Button(self, text="Login", command=self.on_login_click).grid(row=3, column=1)

    def on_signup_click(self):
        signup = SignupWindow()
        signup.mainloop()

    def on_check(self):
        print(self.seller_checkbox.get())

    def on_login_click(self):
        if self.seller_checkbox.get():
            user = Seller(self.entries[0].get(), self.entries[1].get())
        else:
            user = Buyer(self.entries[0].get(), self.entries[1].get())

        if user in get_users():
            self.destroy()
            if user.is_seller():
                SellerMainWindow(user.get_username()).mainloop()
            else:
                BuyerMainWindow(user.get_username()).mainloop()
        else:
            line1 = "The username and password combination does not exist"
            line2 = "Please Sign Up"
            MessageWindow(line1 + "\n" + line2).mainloop()
        

if __name__ == '__main__':
    window = LoginWindow()
    window.mainloop()
