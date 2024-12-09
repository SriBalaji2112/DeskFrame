import customtkinter as tk
import DemoApp.python.ThirdActivity as ThirdActivity
from deskframe.views.ViewBuilder import Builder

class SecondActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = Builder("activity_second.xml", _from=self)
        self.onCreate()

    def onCreate(self):
        # Global Variables Declaration
        btn_text = "Go to 3 window"
        button = self.view.getElementByID("button2")
        button.configure(text=btn_text, command=self.thirdActivity)

    # onClick Methods
    def thirdActivity(self):
        self.Intent(ThirdActivity.ThirdActivity)

    # Switch View -> auto created method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()  # Hide current window
            self.intent(view)  # Show destination window

