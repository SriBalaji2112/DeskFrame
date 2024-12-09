import customtkinter as tk
import DemoApp.python.SecondActivity as SecondActivity
import DemoApp.python.MainActivity as MainActivity
from deskframe.views.ViewBuilder import Builder

class ThirdActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = Builder("activity_third.xml", _from=self)
        self.onCreate()

    def onCreate(self):
        # Global Variables Declaration
        main = self.view.getElementByID("main_activity")
        second = self.view.getElementByID("second_activity")
        main.configure(command=self.mainActivity)
        second.configure(command=self.secondActivity)
        pass

    # onClick methods
    def mainActivity(self):
        self.Intent(MainActivity.MainActivity)

    def secondActivity(self):
        self.Intent(SecondActivity.SecondActivity)

    # Switch View -> auto created method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()               # Hide current window
            self.intent(view)  # Show destination window

