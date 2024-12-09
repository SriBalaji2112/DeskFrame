import customtkinter as tk
from deskframe.values.Values import *
from deskframe.views.ViewBuilder import Builder

class MainActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        # self.view = ViewBuilder(_from=self, context="activity_main.xml"
        self.view = Builder("activity_main.xml", _from=self)
        self.color = Colors()
        self.onCreate()

    def onCreate(self):
        # Global Variables Declaration
        pass
    # onClick Methods

    # Switch View -> auto created method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()               # Hide current window
            self.intent(view)  # Show destination window

