from tkinter import *


class MessageWindow(Tk):
    def __init__(self, warning_msg, warning=True):
        Tk.__init__(self)
        if warning:
            self.title = "Sass-E-Commerce - Warning"
        else:
            self.title = "Sass-E-Commerce - Message"
        Label(self, text=warning_msg).pack()
