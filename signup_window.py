from tkinter import *
from message_window import MessageWindow
from database import *


class SignupWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Sass-E-Commerce - Sign Up")
        self.geometry('320x180')
        self.entries = []
        self.initialize_labels()
        self.initialize_entries()
        self.initialize_signup_button()
        self.seller_check = BooleanVar()
        Checkbutton(self, text="I am a seller", var=self.seller_check, command=self.oncheck).grid(row=2, column=1)

    def oncheck(self):
        print(self.seller_check.get())

    def initialize_labels(self):
        Label(self, text='Username').grid(row=0, column=0)
        Label(self, text='Password').grid(row=1, column=0)

    def initialize_entries(self):
        for i in range(2):
            self.entries.append(Entry(self))
            self.entries[i].grid(row=i, column=1)

    def initialize_signup_button(self):
        b = Button(self, text="Sign Up", command=self.on_signup_click)
        b.grid(row=3, column=1)

    def on_signup_click(self):
        if self.seller_check.get():
            user = Seller(self.entries[0].get(), self.entries[1].get())
        else:
            user = Buyer(self.entries[0].get(), self.entries[1].get())

        if user in get_users():
            warning = MessageWindow("User with username already exists.")
            warning.mainloop()
        else:
            save_user(user)
            self.destroy()
            MessageWindow("User successfully created.", warning=False).mainloop()
