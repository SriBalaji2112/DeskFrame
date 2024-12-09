import customtkinter as tk
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from deskframe.views.ViewBuilder import Builder


class MainActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = Builder("activity_main.xml", _from=self)
        self.onCreate()

    def onCreate(self):
        # Global Variables Declaration
        self.email_id = tk.StringVar()
        self.newPass = tk.StringVar()
        self.mail_id = "sribalaji2112@gmail.com"
        self.password_exist = "SriBalaji"

        email = self.view.getElementByID("email")
        password = self.view.getElementByID("pass")
        login = self.view.getElementByID("login")
        google_btn = self.view.getElementByID("google")
        email.configure(textvariable=self.email_id)
        password.configure(textvariable=self.newPass, show="*")
        login.configure(command=self.checker)


    # onClick Methods
    def checker(self):
        if self.email_id.get() == self.mail_id and self.password_exist == self.newPass.get():
            print("Success...")

    # Switch View -> auto created method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()  # Hide current window
            self.intent(view)  # Show destination window

