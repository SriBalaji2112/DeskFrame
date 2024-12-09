import customtkinter as tk
import DemoApp.python.SecondActivity as SecondActivity
from deskframe.views.notification import Notification
from deskframe.values.Values import *
from deskframe.views.toast import Toast
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
        btn_text = "Hello"
        button = self.view.getElementByID("notify")
        button.configure(command=self.secondActivity)

        toast_button = self.view.getElementByID("toastbtn")
        toast_button.configure(command=self.toastBtn)

    # onClick Methods
    def toastBtn(self):
        toast = Toast()
        toast.makeText(_from=self, message="Toast Button Clicked", waiting_time=toast.LONGLENGTH)

    def secondActivity(self):
        self.Intent(SecondActivity.SecondActivity)
        notify = Notification()
        notify.notify("Test", "This is for testing...")

    # Switch View -> auto created method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()               # Hide current window
            self.intent(view)  # Show destination window

