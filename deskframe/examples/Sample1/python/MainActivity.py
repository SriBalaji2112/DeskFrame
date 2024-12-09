import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import customtkinter as tk
from deskframe.views.ViewBuilder import Builder
from deskframe.views.notification import Notification


class MainActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = Builder(context="activity_main.xml", _from=self)
        self.onCreate()

    def onCreate(self):
        # Global Variables Declaration
        pass

    # onClick Methods

    # Switch View -> auto created InBuild method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()               # Hide current window
            self.intent(view)  # Show destination window

