
# builder.py
import sys
from cx_Freeze import setup, Executable
import xml.etree.ElementTree as ET
from PIL import Image
import pyfiglet
import colorama
from colorama import Fore, Style

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

application_name = "PyDesk2"
discription = "PyDesk2 Application"
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

ascii_pydesk2 = asciiPrint("P Y D E S K 2")
colorPrint(Fore.GREEN, ascii_pydesk2)

setup(
    name=application_name,
    version=version,
    description=discription,
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, target_name=application_name+".exe", icon=icon_name)]
)


