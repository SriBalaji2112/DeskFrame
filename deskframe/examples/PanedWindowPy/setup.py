import argparse
import subprocess

import pyfiglet
import os
import colorama
from colorama import Fore, Style
from main import rootManager

global manager


class CreateActivity:
    def __init__(self, name):
        directory_ = os.getcwd()

        python_dir = os.path.join(directory_, "python")
        res_dir = os.path.join(directory_, "res")
        layout_dir = os.path.join(res_dir, "layout")

        activity_name, layout_name = format_activity_name(name)
        activity_content = f"""
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from deskframe.views.ViewBuilder import Builder
import customtkinter as tk


class {activity_name}(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = Builder(context="{layout_name}.xml", _from=self)
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

        """

        layout_content = """<?xml version="1.0" encoding="UTF-8" ?>
<Layout>

</Layout>
"""
        if os.path.exists(python_dir + "/" + activity_name + ".py"):
            colorPrint(Fore.RED, f"Activity is already exists using this name..")
            exit(1)

        new_file = open(python_dir + "/" + activity_name + ".py", "w")
        new_file.write(activity_content)
        new_file.close()

        layout_file = open(layout_dir + "/" + layout_name + ".xml", "w")
        layout_file.write(layout_content)
        layout_file.close()
        colorPrint(Fore.BLUE, "Activity Created successfully...")
        pass
        

def format_activity_name(name):
    name = name.capitalize()
    if name.endswith("Activity") or name.endswith("activity"):
        return name[:len(name)-8]+"Activity", "activity_"+name[:len(name)-8].lower()
    return name + "Activity", "activity_"+name.lower()
    

def asciiPrint(name):
    # Create an activity by printing the name in ASCII art using pyfiglet.
    ascii_text = pyfiglet.figlet_format(name)
    return ascii_text


def colorPrint(color, name):
    colorama.init()
    print(f"{color}{name}{Style.RESET_ALL}")
    colorama.deinit()


def main():
    ascii_deskframe = asciiPrint("P Y D E S K 2")
    colorPrint(Fore.GREEN, ascii_deskframe)
    
    parser = argparse.ArgumentParser(description="SETUP DESKFRAME PROJECT DIRECTORY")

    parser.add_argument("--createActivity", type=str, help="Create an activity with the specified name.")
    parser.add_argument("--server", nargs=1, help="Start live server for DeskFrame Project")
    parser.add_argument("--buildExe", action="store_true", help="Build the executable file")
    args = parser.parse_args()
    if args.createActivity:
        flag = CreateActivity(args.createActivity)
    elif args.server and args.server[0] == "run":
        rootManager()
    elif args.buildExe:
        subprocess.run(["python", "./builder.py", "build"])
    else:
        print("[ERROR] Please provide a valid option.")
        print("[INFO] python .\setup.py -h")


if __name__ == "__main__":
    main()

