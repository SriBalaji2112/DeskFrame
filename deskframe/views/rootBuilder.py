import os.path
import customtkinter as tk
import xml.etree.ElementTree as ET
from PIL import Image
resize_x = True
resize_y = True
flag = 0


class Builder(tk.CTk):
    def __init__(self, file, _from):
        super().__init__()
        global flag, resize_y, resize_x
        self.file = file
        tree = ET.parse(self.file)
        self.root = tree.getroot()
        self.maxi_flag = 0
        self.width = 100
        self.hight = 100
        self.x_axis = 100
        self.y_axis = 100
        if _from == 0:
            print("Frame not found")
            exit(0)
        else:
            for element in self.root:
                if element.tag == "Application-Name":
                    _from.title(element.text)
                # Appearance Mode
                # Iterate through the XML elements and create tkinter widgets
                if element.tag == "Appearence_Mode":
                    tk.set_appearance_mode(element.text)

                if element.tag == "Color-Theme":
                    # if element.text not in ["blue", "green", "darkgreen"]:
                    #     current_path = os.path.dirname(os.path.realpath(__file__))
                    #     tk.set_default_color_theme(current_path+"/themes/"+element.text+".json")
                    # else:
                    tk.set_default_color_theme(element.text)

                if element.tag == "Alignment":
                    if element.text.lower() == "center":
                        print("center")
                        _from.eval('tk::PlaceWindow . Center')
                if element.tag == "WindowBar":
                    if element.text.lower() == "false":
                        _from.overrideredirect(1)
                if element.tag == "BG-Transparent":
                    if element.text.lower() == "true":
                        _from.attributes('-transparentcolor', 'white')
                if element.tag == "Top-Most":
                    if element.text.lower() == "true":
                        _from.attributes('-topmost', True)
                if element.tag == "Schedule":
                    if element.text.lower() != "none":
                        seconds = element.text * 1000
                        _from.after(seconds, _from.destroy)
                # Full Screen
                if element.tag == "Maximize":
                    if element.text.lower() == "true":
                        self.maxi_flag = 1
                        _from.attributes('-fullscreen', True)

                if element.tag == "Icon":
                    self.icon_name = element.text
                    self.icon_name = "./res/drawable/" + self.icon_name
                    if os.path.exists(self.icon_name):
                        if self.icon_name.endswith(".png"):
                            self.icon_name = self.convert_to_icon(self.icon_name, self.icon_name.replace(".png", ".ico"))
                        elif self.icon_name.endswith(".jpg"):
                            self.icon_name = self.convert_to_icon(self.icon_name, self.icon_name.replace(".jpg", ".ico"))
                        elif self.icon_name.endswith(".jpeg"):
                            self.icon_name = self.convert_to_icon(self.icon_name, self.icon_name.replace(".jpeg", ".ico"))
                        _from.iconbitmap(self.icon_name)

                # Resize
                if element.tag == "Resizable-Width":
                    if element.text.lower() == "false":
                        resize_x = False
                    flag = flag+1
                if element.tag == "Resizable-Height":
                    if element.text.lower() == "false":
                        resize_y = False
                    flag = flag+1
                if flag == 2:
                    _from.resizable(resize_x, resize_y)
                self.which_fun = []
                self.fun_name = []
                # print("Window")
                if self.maxi_flag == 0:
                    if element.tag == 'Layout_Width':
                        self.width = element.text
                    if element.tag == 'Layout_Height':
                        self.hight = element.text
                    if element.tag == 'x':
                        self.x_axis = element.text
                    if element.tag == 'y':
                        self.y_axis = element.text
                    # width, hight, x, y = self.convert_to_pixels(self.width), self.convert_to_pixels(
                    #     self.hight), self.convert_to_pixels(self.x_axis), self.convert_to_pixels(self.y_axis)
                    if (self.hight is not None) and (self.width is not None):
                        if (self.x_axis is not None) and (self.y_axis is not None):
                            _from.geometry(f"{int(self.width)}x{int(self.hight)}+{self.x_axis}+{self.y_axis}")
                        else:
                            _from.geometry(f"{self.width}x{self.hight}+0+0")
                # Grid System
                grid_columnconfig = element.get("column") if element.get("column") is not None else None
                grid_columnsconfig = element.get("columns") if element.get("columns") is not None else None
                grid_rowconfig = element.get("row") if element.get("row") is not None else None
                grid_weight = element.get("weight") if element.get("weight") is not None else None
                grid_rowsconfig = element.get("rows") if element.get("rows") is not None else None

                if element.tag == 'GridRowConfigure':
                    if grid_rowsconfig is not None:
                        for i in [int(coord) for coord in grid_rowsconfig.strip('()').split(',')]:
                            _from.grid_rowconfigure(i, weight=int(grid_weight))
                    if grid_rowconfig is not None:
                        _from.grid_rowconfigure(int(grid_rowconfig), weight=int(grid_weight))
                elif element.tag == 'GridColumnConfigure':
                    if grid_columnsconfig is not None:
                        for i in [int(coord) for coord in grid_columnsconfig.strip('()').split(',')]:
                            _from.grid_columnconfigure(i, weight=int(grid_weight))
                    if grid_columnconfig is not None:
                        _from.grid_columnconfigure(int(grid_columnconfig), weight=int(grid_weight))

    def convert_to_icon(self, input_image_path, output_icon_path):
        try:
            image = Image.open(input_image_path)
            image.save(output_icon_path, format="ICO")
            print(f"Successfully converted {input_image_path} to {output_icon_path}")
            return output_icon_path
        except Exception as e:
            print(f"An error occurred: {e}")

    def convert_to_pixels(self, val):
        if val is None:
            return None
        value, unit = val[:-2], val[-2:]
        if unit == 'px':
            # print(value)
            return int(value)
        elif unit == 'dp':
            # Assuming 1dp = 1.3333px (approximately)
            return int(float(value) * 1.3333)
        else:
            raise ValueError("Invalid unit: " + unit)