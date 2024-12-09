# setup.py
import sys
from cx_Freeze import setup, Executable
import xml.etree.ElementTree as ET
from PIL import Image


class BuildExe:
    def __init__(self):
        self.tree = ET.parse("Config.xml")
        self.root = self.tree.getroot()

        self.application_name = "PyDesk2"
        self.discription = "PyDesk2 Application"
        self.icon_name = "email-icon.png"
        self.version = "v0.0.1"

        for element in self.root:
            if element.tag == "EXE-Name":
                self.application_name = element.text
                self.application_name = self.application_name.replace(" ", "")
            if element.tag == "Discription":
                self.discription = element.text
            if element.tag == "Icon":
                self.icon_name = element.text
                self.icon_name = "./res/drawable/" + self.icon_name
                if self.icon_name.endswith(".png"):
                    self.icon_name = self.convert2Icon(self.icon_name, self.icon_name.replace(".png", ".ico"))
                elif self.icon_name.endswith(".jpg"):
                    self.icon_name = self.convert2Icon(self.icon_name, self.icon_name.replace(".jpg", ".ico"))
                elif self.icon_name.endswith(".jpeg"):
                    self.icon_name = self.convert2Icon(self.icon_name, self.icon_name.replace(".jpeg", ".ico"))
            if element.tag == "Version":
                self.version = element.text
                self.version = self.version.replace("v", "")

        # Dependencies are automatically detected, but it might need fine-tuning.
        build_exe_options = {"packages": ["os", "xml", "PIL", "customtkinter"], "includes": ["res", "main"],
                             "include_files": ["res/", "Config.xml"]}

        # GUI applications require a different base on Windows (the default is for a console application).
        base = None
        if sys.platform == "win32":
            base = "Win32GUI"

        setup(
            name=self.application_name,
            version=self.version,
            description=self.discription,
            options={"build_exe": build_exe_options},
            executables=[Executable("main.py", base=base, target_name=self.application_name+".exe", icon=self.icon_name)]
        )

    def convert2Icon(self, input_image_path, output_icon_path):
        try:
            image = Image.open(input_image_path)
            image.save(output_icon_path, format="ICO")
            print(f"Successfully converted {input_image_path} to {output_icon_path}")
            return output_icon_path
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    BuildExe()
