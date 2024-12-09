import argparse
import os
import time
import pyfiglet
import colorama
from colorama import Fore, Style
from yaspin import yaspin
import subprocess


class CreateProject:
    def __init__(self, name):
        directory_ = os.getcwd()
        name.capitalize()
        project_dir = os.path.join(directory_, name)

        try:
            os.makedirs(project_dir)

        except Exception as e:
            colorPrint(Fore.RED, e)
            colorPrint(Fore.RED, "[ERROR] Project is already exist in this name...")
            exit(1)

        python_dir = os.path.join(project_dir, "python")
        res_dir = os.path.join(project_dir, "res")
        layout_dir = os.path.join(res_dir, "layout")
        drawable_dir = os.path.join(res_dir, "drawable")
        font_dir = os.path.join(res_dir, "font")
        value_dir = os.path.join(res_dir, "values")

        array_dir = [python_dir, res_dir, layout_dir, drawable_dir, font_dir, value_dir]

        spinner = yaspin()
        spinner.start()
        self.createDir(array_dir)
        spinner.stop()

        # spinner.start()
        # self.createVenv(project_dir)
        # spinner.stop()

        init_array = [python_dir, project_dir]
        for _dir in init_array:
            file_init = open(_dir + "/__init__.py", "w")
            if project_dir == _dir:
                file_init.write("__VERSION__ = 'v0.1.0'")
            file_init.close()

        # config_file = open("files/Config.xml", "r")
        config_file = """<?xml version="1.0" encoding="UTF-8" ?>
<Config>
    <Application-Name>DeskFrame Application</Application-Name>
    <Discription>This is DeskFrame application.</Discription>
    <Version>v0.0.1</Version>
    <Icon>email-icon.png</Icon>
    <EXE-Name>demoapp</EXE-Name>
    <Maximize>False</Maximize>
    <Layout_Width>600</Layout_Width>
    <Layout_Height>480</Layout_Height>
    <x>10</x>
    <y>10</y>
    <!-- <Alignment>center</Alignment> -->
    <Appearence_Mode>dark</Appearence_Mode>
    <Color-Theme>blue</Color-Theme>
    <Resizable-Width>False</Resizable-Width>
    <Resizable-Height>False</Resizable-Height>
    <WindowBar>True</WindowBar>
    <BG-Transparent>False</BG-Transparent>
    <Top-Most>False</Top-Most>
    <Schedule>None</Schedule>
</Config>
"""
        config_new_file = open(project_dir + "/Config.xml", "w")
        config_new_file.write(config_file)
        # config_file.close()
        config_new_file.close()
        # main_file = open("files/main.py", "r")
        main_file = """import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import customtkinter as tk
from deskframe.views.rootBuilder import Builder
from python.MainActivity import MainActivity


class WindowManager(tk.CTk):
    def __init__(self):
        super().__init__()
        Builder(file="Config.xml", _from=self)
        self.current_frame = None
        self.switch_frame(MainActivity)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self, intent=self.switch_frame)
        if self.current_frame:
            self.current_frame.pack_forget()  # Hide current frame
        new_frame.pack(expand=True, fill="both")  # Show new frame
        self.current_frame = new_frame


def on_closing():
    manager.withdraw()
    manager.quit()

def rootManager():
    global manager
    manager = WindowManager()
    manager.protocol("WM_DELETE_WINDOW", on_closing)
    manager.mainloop()

if __name__ == "__main__":
    manager = WindowManager()
    manager.protocol("WM_DELETE_WINDOW", on_closing)
    manager.mainloop()
"""
        main_new_file = open(project_dir + "/main.py", "w")
        main_new_file.write(main_file)
        # main_file.clos
        main_new_file.close()

        builder_content = """
# builder.py
import sys
from cx_Freeze import setup, Executable
import xml.etree.ElementTree as ET
from PIL import Image
import colorama
from colorama import Fore, Style
import pyfiglet

def convert2Icon(input_image_path, output_icon_path):
    try:
        image = Image.open(input_image_path)
        image.save(output_icon_path, format="ICO")
        print(f"Successfully converted {input_image_path} to {output_icon_path}")
        return output_icon_path
    except Exception as e:
        print(f"An error occurred: {e}")


tree = ET.parse("Config.xml")
root = tree.getroot()

application_name = "DeskFrame"
discription = "DeskFrame Application"
icon_name = "email-icon.png"
version = "v0.0.1"

for element in root:
    if element.tag == "EXE-Name":
        application_name = element.text
        application_name = application_name.replace(" ", "")
    if element.tag == "Discription":
        discription = element.text
    if element.tag == "Icon":
        icon_name = element.text
        icon_name = "./res/drawable/" + icon_name
        if icon_name.endswith(".png"):
            icon_name = convert2Icon(icon_name, icon_name.replace(".png", ".ico"))
        elif icon_name.endswith(".jpg"):
            icon_name = convert2Icon(icon_name, icon_name.replace(".jpg", ".ico"))
        elif icon_name.endswith(".jpeg"):
            icon_name = convert2Icon(icon_name, icon_name.replace(".jpeg", ".ico"))
    if element.tag == "Version":
        version = element.text
        version = version.replace("v", "")

# Dependencies are automatically detected, but it might need fine-tuning.
build_exe_options = {"packages": ["os", "xml", "PIL", "customtkinter"], "includes": ["res", "main"],
                     "include_files": ["res/", "Config.xml"]}

# GUI applications require a different base on Windows (the default is for a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


def asciiPrint(name):
    # Create an activity by printing the name in ASCII art using pyfiglet.
    ascii_text = pyfiglet.figlet_format(name)
    return ascii_text


def colorPrint(color, name):
    colorama.init()
    print(f"{color}{name}{Style.RESET_ALL}")
    colorama.deinit()

ascii_deskframe = asciiPrint("P Y D E S K 2")
colorPrint(Fore.GREEN, ascii_deskframe)

setup(
    name=application_name,
    version=version,
    description=discription,
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name=application_name+".exe", icon=icon_name)]
)


"""
        build_file = open(project_dir + "/builder.py", "w")
        build_file.write(builder_content)
        build_file.close()

        # setup
        setup_content = """import argparse
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
        activity_content = f\"\"\"
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

        \"\"\"

        layout_content = \"\"\"<?xml version="1.0" encoding="UTF-8" ?>
<Layout>

</Layout>
\"\"\"
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

"""
        setup_file = open(project_dir + "/setup.py", "w")
        setup_file.write(setup_content)
        setup_file.close()

        # main_activity = open("files/MainActivity.py", "r")
        main_activity = """import os
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

"""
        main_new_activity = open(python_dir + "/MainActivity.py", "w")
        main_new_activity.write(main_activity)
        # main_activity.close()
        main_new_activity.close()

        # main_layout = open("files/activity_main.xml", "r")
        main_layout = """<?xml version="1.0" encoding="UTF-8" ?>
<Layout>
    <TextView
        text='DeskFrame World...!'>
        <Pack
            expand="true"/>
    </TextView>
</Layout>
"""
        main_new_layout = open(layout_dir + "/activity_main.xml", "w")
        main_new_layout.write(main_layout)
        # main_layout.close()
        main_new_layout.close()
        string_content = f"""class Strings:
    def __init__(self):
        self.app_name = "{name}"
        self.version = 0.1
        pass
        """
        value_content = f"""class Colors:
    def __init__(self):
        self.green = "#00e676"
        self.red = "#ff1744"
        self.blue = "#1976d2"
        self.yellow = "#ffeb3b"
        self.purple = "#9c27b0"
        self.orange = "#ff9800"
        self.cyan = "#00bcd4"
        self.pink = "#e91e63"
        self.teal = "#009688"
        self.amber = "#ffc107"
        self.indigo = "#3f51b5"
        self.lime = "#cddc39"
        self.deepPurple = "#673ab7"
        self.deepOrange = "#ff5722"
        self.lightBlue = "#03a9f4"
        self.lightGreen = "#8bc34a"
        self.brown = "#795548"
        self.grey = "#9e9e9e"
        self.blueGrey = "#607d8b"
        self.white = "#ffffff"
        self.black = "#000000"
        self.darkGreen = "#006400"
        self.darkRed = "#8b0000"
        self.darkBlue = "#00008b"
        self.darkYellow = "#8b8b00"
        self.darkPurple = "#4b0082"
        self.darkOrange = "#8b4500"
        self.darkCyan = "#008b8b"
        self.darkPink = "#8b0a50"
        self.darkTeal = "#00868b"
        self.darkAmber = "#8b6100"
        self.olive = "#808000"
        self.magenta = "#ff00ff"
        self.skyBlue = "#87ceeb"
        self.salmon = "#fa8072"
        self.silver = "#c0c0c0"
        self.gold = "#ffd700"
        self.bisque = "#ffe4c4"
        self.chocolate = "#d2691e"
        self.crimson = "#dc143c"
        self.fuchsia = "#ff00ff"
        self.ivory = "#fffff0"
        self.lavender = "#e6e6fa"
        self.maroon = "#800000"
        self.navy = "#000080"
        self.turquoise = "#40e0d0"
        self.violet = "#ee82ee"
        self.wheat = "#f5deb3"
        self.plum = "#dda0dd"
        self.linen = "#faf0e6"
        self.coral = "#ff7f50"
        self.paleGreen = "#98fb98"
        self.slateGray = "#708090"
        self.orchid = "#da70d6"
        self.cadetBlue = "#5f9ea0"
        self.darkSalmon = "#e9967a"
        self.dimGray = "#696969"
        self.fireBrick = "#b22222"
        self.honeydew = "#f0fff0"
        self.lightCoral = "#f08080"
        self.mediumAquamarine = "#66cdaa"
        self.mintCream = "#f5fffa"
        self.navyBlue = "#000080"
        self.papayaWhip = "#ffefd5"
        self.rosyBrown = "#bc8f8f"
        self.saddleBrown = "#8b4513"
        self.sienna = "#a0522d"
        self.thistle = "#d8bfd8"
        self.tomato = "#ff6347"
        self.moccasin = "#ffe4b5"
        self.navajoWhite = "#ffdead"
        self.paleGoldenRod = "#eee8aa"
        self.slateBlue = "#6a5acd"
        self.springGreen = "#00ff7f"
        self.steelBlue = "#4682b4"
        self.tan = "#d2b48c"
        self.violetRed = "#d02090"
        self.yellowGreen = "#9acd32"
        self.indianRed = "#cd5c5c"
        self.darkGoldenRod = "#b8860b"
        self.lawnGreen = "#7cfc00"
        self.darkOrchid = "#9932cc"
        self.snow = "#fffafa"
        self.peru = "#cd853f"
        self.royalBlue = "#4169e1"
        self.lemonChiffon = "#fffacd"
        self.mediumSeaGreen = "#3cb371"
        self.mediumOrchid = "#ba55d3"
        self.darkSlateGray = "#2f4f4f"
        self.tan = "#d2b48c"
        self.darkKhaki = "#bdb76b"
        self.slateGrey = "#708090"
        self.slateBlue = "#6a5acd"
        self.darkViolet = "#9400d3"
        self.mediumSlateBlue = "#7b68ee"
        self.mediumOrchid = "#ba55d3"
        self.lightSkyBlue = "#87cefa"
        self.lavenderBlush = "#fff0f5"
        self.paleVioletRed = "#db7093"
        self.cornsilk = "#fff8dc"
        self.beige = "#f5f5dc"
        self.azure = "#f0ffff"
        self.honeydew = "#f0fff0"
        self.aliceBlue = "#f0f8ff"
        self.oldLace = "#fdf5e6"
        self.seaShell = "#fff5ee"
        self.linen = "#faf0e6"
        self.mintCream = "#f5fffa"
        self.floralWhite = "#fffaf0"
        self.gainsboro = "#dcdcdc"
        self.antiqueWhite = "#faebd7"
        self.navajoWhite = "#ffdead"
        self.ghostWhite = "#f8f8ff"
        self.papayaWhip = "#ffefd5"
        self.blanchedAlmond = "#ffebcd"
        self.bisque = "#ffe4c4"
        self.peachPuff = "#ffdab9"
        self.wheat = "#f5deb3"
        self.mistyRose = "#ffe4e1"
        self.lavender = "#e6e6fa"
        self.burlyWood = "#deb887"
        self.khaki = "#f0e68c"
        self.paleGoldenRod = "#eee8aa"
        self.aqua = "#00ffff"
        self.aquamarine = "#7fffd4"
        self.mediumTurquoise = "#48d1cc"
        self.paleTurquoise = "#afeeee"
        self.darkTurquoise = "#00ced1"
        self.cyan = "#00ffff"
        self.lightCyan = "#e0ffff"
        self.azure = "#f0ffff"
        self.darkCyan = "#008b8b"
        self.teal = "#008080"
        self.darkSlateBlue = "#483d8b"
        """
        value_new_file = open(value_dir + "/Values.py", "w")
        string_new_file = open(value_dir + "/Strings.py", "w")
        value_new_file.write(value_content)
        string_new_file.write(string_content)
        string_new_file.close()
        value_new_file.close()

        colorPrint(Fore.GREEN, "[INFO] PROJECT CREATED SUCCESSFULLY...")

    @yaspin(text="Creating Project Directory...")
    def createDir(self, array_dir):
        for _dir in array_dir:
            os.makedirs(_dir)
            time.sleep(0.5)


def asciiPrint(name):
    """Create an activity by printing the name in ASCII art using pyfiglet."""
    ascii_text = pyfiglet.figlet_format(name)
    return ascii_text


def colorPrint(color, name):
    colorama.init()
    print(f"{color}{name}{Style.RESET_ALL}")
    colorama.deinit()

def main():
    deskframe_name = asciiPrint("D E S K F R A M E")
    colorPrint(Fore.BLUE, deskframe_name)
    parser = argparse.ArgumentParser(description="Create an activity in DeskFrame.")

    # Add the startProject argument without the -- prefix
    parser.add_argument("--startProject", type=str, help="Start a project with the specified name.")
    parser.add_argument("--buildExe", type=str, help="Build exe file")
    # Parse arguments
    args = parser.parse_args()

    # Check if project_name is provided
    if args.startProject:
        CreateProject(args.startProject)
    else:
        colorPrint(Fore.RED, "[ERROR] Please provide a valid project name.")

if __name__ == "__main__":
    main()