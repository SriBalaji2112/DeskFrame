import argparse
import pyfiglet
import os
import colorama
from colorama import Fore, Style
from main import rootManager

global manager


class CreateActivity:
    def __init__(self, activity_name):
        directory_ = os.getcwd()

        python_dir = os.path.join(directory_, "python")
        res_dir = os.path.join(directory_, "res")
        layout_dir = os.path.join(res_dir, "layout")

        layout_name = activity_name.replace("Activity", "")
        layout_name = "activity_" + layout_name.lower()
        activity_content = f"""
import customtkinter as tk

class {activity_name}(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.intent = intent
        self.view = self.setContextView("{layout_name}.xml")
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

        layout_content = """
<?xml version="1.0" encoding="UTF-8" ?>
<Layout>

</Layout>
"""
        if activity_name.lower().endswith('activity'):
            activity_name = activity_name.title()
        else:
            activity_name = f"{activity_name.title()}Activity"
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


def asciiPrint(name):
    """Create an activity by printing the name in ASCII art using pyfiglet."""
    ascii_text = pyfiglet.figlet_format(name)
    print(ascii_text)


def colorPrint(color, name):
    colorama.init()
    print(f"{color}{name}{Style.RESET_ALL}")
    colorama.deinit()


def main():
    """Main function to handle CLI arguments."""

    parser = argparse.ArgumentParser(description="SETUP PYDESK2 PROJECT DIRECTORY")

    parser.add_argument("--createActivity", type=str, help="Create an activity with the specified name.")
    parser.add_argument("--server", nargs=1, help="Start live server for PyDesk2 Project")
    args = parser.parse_args()
    if args.createActivity:
        flag = CreateActivity(args.create_activity)
    elif args.server[0] == "run":
        rootManager()
    else:
        print("[ERROR] Please provide a valid option.")
        print("[INFO] python .\setup.py -h")


if __name__ == "__main__":
    main()
