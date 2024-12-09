import threading
import time
import customtkinter as tk
# import CTkListbox
from tkinter import ttk
import xml.etree.ElementTree as ET
from PIL import Image
# from tkinter_webcam import webcam
from deskframe.Tools.Menu import Menu
from deskframe.Tools.ToolBar import ToolBar
# from deskframe.values.Symbols import Symbols
import deskframe.Tools.VideoFrame as VideoFrame
object = ''
pervious_object = []

class Builder:
    def __init__(self, context, _from=0):
        self.object_id = {}
        self.context = context
        file = "./res/layout/" + self.context.replace('.py', '.xml')
        self.current_xml_content = self.read_xml_file(file)
        self.contextView(self.context, _from)

        # Start a thread to periodically check for XML updates
        self.thread = threading.Thread(target=self.check_for_updates, args=(_from,))
        self.thread.daemon = True
        self.thread.start()

    def check_for_updates(self, _from):
        while True:
            # Read the XML content from the file
            file = "./res/layout/" + self.context.replace('.py', '.xml')
            updated_xml_content = self.read_xml_file(file)

            # Check if XML content has changed
            if updated_xml_content != self.current_xml_content:
                self.current_xml_content = updated_xml_content
                # Update the layout
                _from.after(0, self.contextView, self.context, _from)  # Use after method to update the GUI
            time.sleep(0.1)  # Check every 2 seconds

    def read_xml_file(self, filename):
        # Read XML content from the file
        with open(filename, 'r') as file:
            return file.read()

    object = ''
    def contextView(self, context, _from=0):
        # Clear previous widgets
        for widget in _from.winfo_children():
            widget.destroy()
        # Get XML elements
        self.file = "./res/layout/" + context.replace('.py', '.xml')

        tree = ET.parse(self.file)
        self.root = tree.getroot()
        if _from == 0:
            print("Frame not found")
            exit(0)
        else:
            for element in self.root:
                #Grid System
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

                # Grid Config
                if element.tag == 'GridRowConfigure' or element.tag == 'GridColumnConfigure':
                    continue
                self.create_widget(_from, element)

            style = ttk.Style()
            if tk.get_appearance_mode().lower() == "dark":
                # Configure the style to have a dark theme
                style.theme_use('clam')
            else:
                style.theme_use('default')

    def setContextView(self, context):
        self.context = context
        file = "./res/layout/" + self.context.replace('.py', '.xml')
        self.current_xml_content = self.read_xml_file(file)
        self.contextView(self.context)

        # Start a thread to periodically check for XML updates
        self.thread = threading.Thread(target=self.check_for_updates)
        self.thread.daemon = True
        self.thread.start()

    # Function to convert units to pixels
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

    def getElementByID(self, identity):
        try:
            return self.object_id[identity]
        except Exception as E:
            print("There is no Id in the name of:", identity)
            print(E)

    # Function to create a tkinter widget based on an XML element
    def create_widget(self, parent, element, pw=0):
        global object, pervious_object

        def settings(self, object, video=0):
            global pervious_object
            # # Configuration Settings
            if put_operation == "pack":
                object.pack()
            if set_default_value is not None:
                object.set(set_default_value)
            if src is not None:
                object.load(src)
            if always_play.lower() == "true":
                object.play()
            if add_tab is not None:
                for item in add_tab:
                    object.add(item)
            if border_width is not None:
                object.configure(border_width=border_width)
            if border_spacing is not None:
                object.configure(border_spacing=border_spacing)
            if hover_color is not None:
                object.configure(hover_color=hover_color)
            if border_color is not None:
                object.configure(border_color=border_color)
            if font_color is not None:
                object.configure(text_color=font_color)
            if text_color_disable is not None:
                object.configure(text_color_disabled=text_color_disable)
            if state is not None:
                object.configure(state=state)
            if hover_visible is not None:
                object.configure(hover=hover_visible)
            if img is not None:
                img_data = Image.open(img)
                pg = tk.CTkImage(img_data)
                object.configure(image=pg)
            if compound is not None:
                object.configure(compound=compound)
            if width is not None:
                object.configure(width=width)
            if font_element is not None:
                object.configure(font=font_element)
            if height is not None:
                object.configure(height=height)
            if text is not None:
                # symbols_instance = Symbols()
                # if text.startswith("\\"):
                #     # for attribute in dir(symbols_instance):
                #     #     if not attribute.startswith('__'):  # Exclude internal attributes
                #     #         # print(f"{attribute}: {getattr(symbols_instance, attribute)}")
                #     #         if text.replace("\\", "") == attribute:
                #     # object.configure(text=getattr(symbols_instance, text.replace("\\", "")))
                #     pass
                # else:
                object.configure(text=text)
            if corner_radius is not None:
                object.configure(corner_radius=corner_radius)
            if foreground_color is not None:
                object.configure(fg_color=foreground_color)
            if font_color is not None:
                object.configure(text_color=font_color)
            if anchor is not None:
                object.configure(anchor=anchor)
            if compound is not None:
                object.configure(compound=compound)
            if justify is not None:
                object.configure(justify=justify)
            if padding_x is not None:
                object.configure(padx=padding_x)
            if padding_y is not None:
                object.configure(pady=padding_y)
            if dropdown_foreground_color is not None:
                object.configure(dropdown_fg_color=dropdown_foreground_color)
            if dropdown_hover_color is not None:
                object.configure(dropdown_hover_color=dropdown_hover_color)
            if dropdown_text_color is not None:
                object.configure(dropdown_text_color=dropdown_text_color)
            if values is not None:
                object.configure(values=coordinates_list)
            if placeholder_color is not None:
                object.configure(placeholder_text_color=placeholder_color)
            if placeholder_text is not None:
                object.configure(placeholder_text=placeholder_text)
            if dropdown_font_color is not None:
                object.configure(dropdown_text_color=dropdown_font_color)
            if dropdown_font is not None:
                object.configure(dropdown_font=dropdown_font)
            if resizing is not None:
                object.configure(dynamic_resizing=resizing)
            if progress_color is not None:
                object.configure(progress_color=progress_color)
            # if orientation is not None:
            #     object.configure(orientation=orientation)
            if mode is not None:
                object.configure(mode=mode)
            if determinate_speed is not None:
                object.configure(determinate_speed=determinate_speed)
            if indeterminate_speed is not None:
                object.configure(indeterminate_speed=indeterminate_speed)
            if radiobutton_width is not None:
                object.configure(radiobutton_width=radiobutton_width)
            if radiobutton_height is not None:
                object.configure(radiobutton_height=radiobutton_height)
            if border_width_unchecked is not None:
                object.configure(border_width_unchecked=border_width_unchecked)
            if border_width_checked is not None:
                object.configure(border_width_checked=border_width_checked)
            if scrollbar_foreground_color is not None:
                object.configure(scrollbar_fg_color=scrollbar_foreground_color)
            if scrollbar_button_color is not None:
                object.configure(scrollbar_button_color=scrollbar_button_color)
            if scrollbar_button_hover_color is not None:
                object.configure(scrollbar_button_hover_color=scrollbar_button_hover_color)
            if label_foreground_color is not None:
                object.configure(label_fg_color=label_foreground_color)
            if lable_text_color is not None:
                object.configure(lable_text_color=lable_text_color)
            if lable_text is not None:
                object.configure(label_text=lable_text)
            if label_font is not None:
                object.configure(label_font=label_font)
            if label_anchor is not None:
                object.configure(label_anchor=label_anchor)
            if minimum_pixel_length is not None:
                object.configure(minimum_pixel_length=minimum_pixel_length)
            if selected_color is not None:
                object.configure(selected_color=selected_color)
            if selected_hover_color is not None:
                object.configure(selected_hover_color=selected_hover_color)
            if unselected_color is not None:
                object.configure(unselected_color=unselected_color)
            if unselected_hover_color is not None:
                object.configure(unselected_hover_color=unselected_hover_color)
            if from_ != 0:
                object.configure(from_=int(from_))
            if to_ != 1:
                object.configure(to=int(to_))
            if number_of_steps is not None:
                object.configure(number_of_steps=int(number_of_steps))
            if background_color is not None:
                object.configure(bg_color=background_color)
            if switch_width is not None:
                object.configure(switch_width=switch_width)
            if switch_height is not None:
                object.configure(switch_height=switch_height)
            if button_hover_color is not None:
                object.configure(button_hover_color=button_hover_color)
            if segmented_button_foreground_color is not None:
                object.configure(segmented_button_fg_color=segmented_button_foreground_color)
            if segmented_button_selected_color is not None:
                object.configure(segmented_button_selected_color=segmented_button_selected_color)
            if segmented_button_selected_hover_color is not None:
                object.configure(segmented_button_selected_hover_color=segmented_button_selected_hover_color)
            if segmented_button_unselected_color is not None:
                object.configure(segmented_button_unselected_color=segmented_button_unselected_color)
            if segmented_button_unselected_hover_color is not None:
                object.configure(segmented_button_unselected_hover_color=segmented_button_unselected_hover_color)
            if activate_scrollbars is not None:
                object.configure(activate_scrollbars=activate_scrollbars)
            if wrap is not None:
                object.configure(wraplength=wrap)
            # Calender Settings

            if _id is not None:
                self.object_id[_id] = object
            if pw == 1:
                pervious_object.append(object)
            return object

        # ID
        _id = element.get('id') if element.get("id") is not None else None
        # Get Width
        width = element.get('layout_width') if element.get("layout_width") is not None else None
        height = element.get('layout_height') if element.get("layout_height") is not None else None
        # Convert into PX
        width = self.convert_to_pixels(width)
        height = self.convert_to_pixels(height)
        x = element.get('x') if element.get("x") is not None else None
        y = element.get('y') if element.get("y") is not None else None
        x = self.convert_to_pixels(x)
        y = self.convert_to_pixels(y)
        put_operation = element.get('push') if element.get("push") is not None else None

        # Radio Button
        radiobutton_width = element.get("radiobutton_width") if element.get(
            "radiobutton_width") is not None else None
        radiobutton_height = element.get("radiobutton_height") if element.get(
            "radiobutton_height") is not None else None
        border_width_unchecked = element.get("border_width_unchecked") if element.get(
            "border_width_unchecked") is not None else None
        border_width_checked = element.get("border_width_checked") if element.get(
            "border_width_checked") is not None else None
        lable_text_color = element.get("lable_text_color") if element.get(
            "lable_text_color") is not None else None
        lable_text = element.get("label_text") if element.get(
            "label_text") is not None else None
        label_font = element.get("label_font") if element.get(
            "label_font") is not None else None
        label_anchor = element.get("label_anchor") if element.get(
            "label_anchor") is not None else None
        minimum_pixel_length = element.get("minimum_pixel_length") if element.get(
            "minimum_pixel_length") is not None else None
        resizing = element.get("resizing") if element.get(
            "resizing") is not None else None

        # Text and Font Section
        # Get Text from XML element
        entry_type = element.get('type') if element.get('type') is not None else None
        text = element.get("text") if element.get("text") is not None else None
        font_ele = element.get('font') if element.get('font') is not None else None
        font_size = element.get('font_size') if element.get('font_size') is not None else None
        font_style = element.get("font_style") if element.get('font_style') is not None else None
        font_weight = element.get("font_weight") if element.get('font_weight') is not None else None
        dropdown_font = element.get("dropdown_font") if element.get('dropdown_font') is not None else None
        values = element.get("values") if element.get('values') is not None else None
        if values is not None:
            coordinates_list = [coord for coord in values.strip('()').split(',')]

        font_size = self.convert_to_pixels(font_size)

        # Corner Radius
        corner_radius = element.get("radius") if element.get('radius') is not None else None
        corner_radius = self.convert_to_pixels(corner_radius)
        anchor = element.get("anchor") if element.get('anchor') is not None else None
        compound = element.get("compound") if element.get('compound') is not None else None
        justify = element.get("justify") if element.get('justify') is not None else None
        pad_x = element.get("padding_x") if element.get('padding_x') is not None else None
        pad_y = element.get("padding_y") if element.get('padding_y') is not None else None
        if pad_x is not None:
            if "(" in pad_x:
                pad_x = [coord for coord in pad_x.strip('()').split(',')]
                for i in range(len(pad_x)):
                    pad_x[i] = self.convert_to_pixels(pad_x[i])
        if pad_y is not None:
            if "(" in pad_y:
                pad_y = [coord for coord in pad_y.strip('()').split(',')]
                for i in range(len(pad_y)):
                    pad_y[i] = self.convert_to_pixels(pad_y[i])

        padding_x = pad_x
        padding_y = pad_y

        # Slider
        from_ = element.get("from_") if element.get('from_') is not None else 0
        to_ = element.get("to_") if element.get('to_') is not None else 1
        number_of_steps = element.get("number_of_steps") if element.get('number_of_steps') is not None else None

        # Switch
        switch_width = element.get("switch_width") if element.get('switch_width') is not None else None
        switch_height = element.get("switch_height") if element.get('switch_height') is not None else None

        # TabView
        add_tab = element.get("add_tabs") if element.get('add_tabs') is not None else None
        tab_text = element.get("tab_text") if element.get("tab_text") is not None else None
        if add_tab is not None:
            add_tab = [coord for coord in add_tab.strip('()').split(',')]
        segmented_button_foreground_color = element.get("segmented_button_foreground_color") if element.get(
            'segmented_button_foreground_color') is not None else None
        segmented_button_selected_color = element.get("segmented_button_selected_color") if element.get(
            'segmented_button_selected_color') is not None else None
        segmented_button_selected_hover_color = element.get("segmented_button_selected_hover_color") if element.get(
            'segmented_button_selected_hover_color') is not None else None
        segmented_button_unselected_color = element.get("segmented_button_unselected_color") if element.get(
            'segmented_button_unselected_color') is not None else None
        segmented_button_unselected_hover_color = element.get(
            "segmented_button_unselected_hover_color") if element.get(
            'segmented_button_unselected_hover_color') is not None else None
        placeholder_text = element.get("placeholder") if element.get(
            "placeholder") is not None else None

        # Color
        foreground_color = element.get('foreground_color') if element.get('foreground_color') is not None else None
        background_color = element.get('background_color') if element.get('background_color') is not None else None
        hover_color = element.get('hover_color') if element.get('hover_color') is not None else None
        button_color = element.get('button_color') if element.get('button_color') is not None else None
        button_hover_color = element.get('button_hover_color') if element.get(
            'button_hover_color') is not None else None
        border_color = element.get('border_color') if element.get('border_color') is not None else None
        progress_color = element.get('progress_color') if element.get('progress_color') is not None else None
        placeholder_color = element.get('placeholder_color') if element.get(
            'placeholder_color') is not None else None
        font_color = element.get('font_color') if element.get('font_color') is not None else None
        selected_color = element.get('selected_color') if element.get('selected_color') is not None else None
        unselected_color = element.get('unselected_color') if element.get('unselected_color') is not None else None
        selected_hover_color = element.get('selected_hover_color') if element.get(
            'selected_hover_color') is not None else None
        unselected_hover_color = element.get('unselected_hover_color') if element.get(
            'unselected_hover_color') is not None else None
        text_color_disable = element.get('text_color_disable') if element.get(
            'text_color_disable') is not None else None
        dropdown_foreground_color = element.get('dropdown_foreground_color') if element.get(
            'dropdown_foreground_color') is not None else None
        dropdown_text_color = element.get('dropdown_text_color') if element.get(
            'dropdown_text_color') is not None else None
        dropdown_hover_color = element.get('dropdown_hover_color') if element.get(
            'dropdown_hover_color') is not None else None
        dropdown_font_color = element.get('dropdown_font_color') if element.get(
            'dropdown_font_color') is not None else None
        scrollbar_foreground_color = element.get('scrollbar_foreground_color') if element.get(
            'scrollbar_foreground_color') is not None else None
        scrollbar_button_color = element.get('scrollbar_button_color') if element.get(
            'scrollbar_button_color') is not None else None
        scrollbar_button_hover_color = element.get('scrollbar_button_hover_color') if element.get(
            'scrollbar_button_hover_color') is not None else None
        label_foreground_color = element.get('label_foreground_color') if element.get(
            'label_foreground_color') is not None else None

        # TextBox
        activate_scrollbars = element.get('activate_scrollbars') if element.get(
            'activate_scrollbars') is not None else None
        wrap = element.get('wrap') if element.get('wrap') is not None else None

        # Image
        img = element.get('img') if element.get('img') is not None else None
        img_compound = element.get('img_compound') if element.get('img_compound') is not None else None
        img_anchor = element.get('img_anchor') if element.get('img_anchor') is not None else None

        # ProgressBar Orientation
        orientation = element.get('orientation') if element.get('orientation') is not None else 'horizontal'
        mode = element.get('mode') if element.get('mode') is not None else None
        determinate_speed = element.get('determinate_speed') if element.get(
            'determinate_speed') is not None else None
        indeterminate_speed = element.get('indeterminate_speed') if element.get(
            'indeterminate_speed') is not None else None

        # Visible & Disable
        state = element.get('state') if element.get('state') is not None else None
        hover_visible = element.get('hover_visible') if element.get('hover_visible') is not None else None
        text_color_disable = element.get('text_color_disable') if element.get(
            'text_color_disable') is not None else None

        # border
        border_width = element.get('border_width') if element.get('border_width') is not None else None
        border_spacing = element.get('border_spacing') if element.get('border_spacing') is not None else None
        border_width = self.convert_to_pixels(border_width)
        border_spacing = self.convert_to_pixels(border_spacing)
        # Grid System
        grid_columnconfig = element.get("column") if element.get("column") is not None else None
        grid_columnsconfig = element.get("columns") if element.get("columns") is not None else None
        grid_rowconfig = element.get("row") if element.get("row") is not None else None
        grid_weight = element.get("weight") if element.get("weight") is not None else None
        grid_rowsconfig = element.get("rows") if element.get("rows") is not None else None

        # Grid
        grid_row = element.get("row") if element.get("row") is not None else None
        grid_column = element.get("column") if element.get("column") is not None else None
        grid_rowspan = element.get("rowspan") if element.get("rowspan") is not None else None
        grid_columnspan = element.get("columnspan") if element.get("columnspan") is not None else None
        sticky = element.get("sticky") if element.get("sticky") is not None else None
        fill = element.get("fill") if element.get("fill") is not None else None
        ipad_x = element.get("internal_padding_x") if element.get("internal_padding_x") is not None else None
        ipad_y = element.get("internal_padding_y") if element.get("internal_padding_y") is not None else None

        # Default
        set_default_value = element.get("set") if element.get("set") is not None else None

        index = element.get('index') if element.get('index') is not None else None
        value = element.get('value') if element.get('value') is not None else None
        # Image
        dark_image = element.get('dark_image') if element.get('dark_image') is not None else None
        light_image = element.get('light_image') if element.get('light_image') is not None else None

        dark_image = "./res/drawable/" + dark_image if dark_image is not None else None
        light_image = "./res/drawable/" + light_image if light_image is not None else None
        img = "./res/drawable/" + img if img is not None else None
        # pack
        side = element.get('side') if element.get('side') is not None else None
        expand = element.get('expand') if element.get('expand') is not None else None
        webcam_index = element.get('index') if element.get('index') is not None else None
        insert_method = element.get('insert') if element.get('insert') is not None else None

        src = element.get('src') if element.get('src') is not None else None
        src = "./res/drawable/" + src if src is not None else None
        always_play = element.get('always_play') if element.get('always_play') is not None else "false"

        # Menu Bar
        seperate_window = element.get('seperate_window') if element.get("seperate_window") is not None else 0
        hover_bg_color = element.get('hover_background_color') if element.get('hover_background_color') is not None \
            else ""
        hover_fg_color = element.get('hover_foreground_color') if element.get('hover_foreground_color') is not None \
            else ""

        if expand is not None:
            if expand.lower() == 'true':
                expand = True
            elif expand.lower() == 'false':
                expand = False
            else:
                pass

        flag = element.get('flag') if element.get('flag') is not None else None

        from deskframe.Tools.font import get_font
        if text is not None:
            font_element = get_font(font_ele, font_size, font_style, font_weight)
        else:
            font_element = None

        if element.tag == 'LinearLayout':
            for child in element:
                self.create_widget(object, child)

        elif element.tag == "include":
            src = element.get('src') if element.get('src') is not None else None
            if src.endswith(".xml"):
                include_file = "./res/" + src
            else:
                include_file = "./res/" + src + ".xml"

            include_tree = ET.parse(include_file)
            include_root = include_tree.getroot()
            for element in include_root:
                self.create_widget(parent, element)

        elif element.tag == "include_menu":
            src = element.get('src') if element.get('src') is not None else None
            if src.endswith(".xml"):
                include_file = "./res/menu/" + src
            else:
                include_file = "./res/menu/" + src + "xml"

            include_tree = ET.parse(include_file)
            include_root = include_tree.getroot()
            for element in include_root:
                self.create_widget(parent, element)

        elif element.tag == 'Frame':
            frame_object = tk.CTkFrame(parent)
            frame_object = settings(self, frame_object)
            for child in element:
                self.create_widget(frame_object, child)

        elif element.tag == 'ImageView':
            if img is not None:
                img_data = Image.open(img)
                img = None
                _img = tk.CTkImage(dark_image=img_data, light_image=img_data, size=(width, height))
            else:
                dark_img_data = Image.open(dark_image)
                light_img_data = Image.open(light_image)
                _img = tk.CTkImage(dark_image=dark_img_data, light_image=light_img_data, size=(width, height))
            image_label = tk.CTkLabel(parent, text="", image=_img)
            image_label = settings(self, image_label)
            for child in element:
                self.create_widget(image_label, child)

        elif element.tag == 'TextView':
            text_object = tk.CTkLabel(parent)
            text_object = settings(self, text_object)
            for child in element:
                self.create_widget(text_object, child)

        elif element.tag == 'Button':
            button_object = tk.CTkButton(parent)
            if text is None:
                text = "DeskFrame"
            button_object = settings(self, button_object)
            for child in element:
                self.create_widget(button_object, child)

        elif element.tag == "CheckBox":
            checkbutton_object = tk.CTkCheckBox(parent)
            checkbutton_object = settings(self, checkbutton_object)
            for child in element:
                self.create_widget(checkbutton_object, child)

        elif element.tag == "WebCam":
            webcam_object = webcam.Box(parent,
                                       width=width,
                                       height=height,
                                       camera_index=webcam_index,
                                       row=grid_row,
                                       colm=grid_column, x=x, y=y, insert=insert_method)
            webcam_object.show_frames()

        elif element.tag == "Entry":
            entry_object = tk.CTkEntry(parent)
            entry_object = settings(self, entry_object)
            for child in element:
                self.create_widget(entry_object, child)
            pass

        elif element.tag == "VideoView":
            # video_object = TkinterVideo(parent, scaled=True)
            video_object = VideoFrame.VideoPlayerApp(parent)
            video_object.configure(bg="black")
            video_object = settings(self, video_object)
            for child in element:
                self.create_widget(video_object, child)

        # podala
        elif element.tag == "ListBox":
            listbox_object = CTkListbox.CTkListbox(parent)
            listbox_object = settings(self, listbox_object)
            for child in element:
                self.create_widget(listbox_object, child)
            pass

        elif element.tag == "MenuButton":
            print("MenuButton is upgrade in Future, PLease use OptionButton")
            pass

        elif element.tag == "Menu":
            menu_object = Menu(parent)
            for child in element:
                self.create_widget(menu_object, child)
            pass

        elif element.tag == "MenuTitle":
            menu_title = parent.menu_bar(text=text, tearoff=seperate_window)
            if _id is not None:
                self.object_id[_id] = menu_title
            for child in element:
                self.create_widget(menu_title, child)

        elif element.tag == "SubTitle":
            parent.add_command(label=text, background=background_color, foreground=foreground_color,
                               activeforeground=hover_fg_color, activebackground=hover_bg_color)

        elif element.tag == "Seperator":
            parent.add_separator()

        elif element.tag == "ToolBar":
            # foreground_color = background_color if foreground_color is None else foreground_color
            toolbar_object = ToolBar(parent)
            toolbar_object = settings(self, toolbar_object)
            toolbar_object.pack(fill="x")
            for child in element:
                toolbar_side = child.get('position') if child.get('position') is not None else None
                if toolbar_side == 'right':
                    self.create_widget(toolbar_object.right_frame, child)
                elif toolbar_side == 'left':
                    self.create_widget(toolbar_object.left_frame, child)
                else:
                    self.create_widget(toolbar_object, child)

        elif element.tag == "Message":
            pass

        elif element.tag == "RadioButton":
            radiobutton_object = tk.CTkRadioButton(parent)
            radiobutton_object = settings(self, radiobutton_object)
            for child in element:
                self.create_widget(radiobutton_object, child)
            pass

        # podala
        elif element.tag == "Scale":
            label_scale = ttk.Scale(parent, from_=int(from_), to=int(to_), orient=orientation)
            label_scale = settings(self, label_scale)
            for child in element:
                self.create_widget(label_scale, child)
            pass

        elif element.tag == "LabeledScale":
            label_scale = ttk.LabeledScale(parent, from_=int(from_), to=int(to_))
            label_scale = settings(self, label_scale)
            for child in element:
                self.create_widget(label_scale, child)

        elif element.tag == "Scrollbar":
            scrollbar_object = tk.CTkScrollbar(parent, orientation=orientation)
            scrollbar_object = settings(self, scrollbar_object)
            for child in element:
                self.create_widget(scrollbar_object, child)
            pass

        elif element.tag == "NoteBook":
            notebook_object = ttk.Notebook(parent)
            notebook_object = settings(self, notebook_object)
            for child in element:
                self.create_widget(notebook_object, child)

        # podala
        elif element.tag == "TopLevel":
            pass

        # podala
        elif element.tag == "SpinBox":
            spinbox_object = ttk.Spinbox(parent)
            spinbox_object = settings(self, spinbox_object)
            for child in element:
                self.create_widget(spinbox_object, child)
            pass

        elif element.tag == "Item":
            parent.insert(index, value)

        elif element.tag == "TreeView":
            tree_object = ttk.Treeview(parent)
            tree_object = settings(self, tree_object)
            for child in element:
                self.create_widget(tree_object, child)

        elif element.tag == "PanedFrame":
            if orientation is not None:
                panedwindow_object = ttk.Panedwindow(parent, orient=orientation)
            else:
                panedwindow_object = ttk.Panedwindow(parent)
            for child in element:
                self.create_widget(panedwindow_object, child, pw=1)
            for i in pervious_object:
                print(i)
                if "panedwinow" in str(i):
                    print("PanedWindow")
                    panedwindow_object.add(i, weight=1)
                else:
                    panedwindow_object.add(i, weight=1)
            pervious_object = []
            pass

        elif element.tag == "ComboBox":
            combobox_object = tk.CTkComboBox(parent)
            combobox_object = settings(self, combobox_object)
            for child in element:
                self.create_widget(combobox_object, child)

        elif element.tag == "OptionMenu":
            optionmenu_object = tk.CTkOptionMenu(parent)
            optionmenu_object = settings(self, optionmenu_object)
            for child in element:
                self.create_widget(optionmenu_object, child)

        elif element.tag == "ProgressBar":
            if orientation is not None:
                progressbar_object = tk.CTkProgressBar(parent, orientation=orientation)
            else:
                progressbar_object = tk.CTkProgressBar(parent)
            progressbar_object = settings(self, progressbar_object)
            for child in element:
                self.create_widget(progressbar_object, child)

        # podala
        elif element.tag == "ScrollableFrame":
            scrollbar_frame_object = tk.CTkScrollableFrame(parent)
            scrollbar_frame_object = settings(self, scrollbar_frame_object)
            for child in element:
                self.create_widget(scrollbar_frame_object, child)
            pass

        elif element.tag == "ScrollBar":
            scrollbar_object = tk.CTkScrollbar(parent)
            scrollbar_object = settings(self, scrollbar_object)
            for child in element:
                self.create_widget(scrollbar_object, child)

        elif element.tag == "SegmentedButton":
            segmentedbutton_object = tk.CTkSegmentedButton(parent)
            segmentedbutton_object = settings(self, segmentedbutton_object)
            for child in element:
                self.create_widget(segmentedbutton_object, child)

        elif element.tag == "Slider":
            slider_object = tk.CTkSlider(parent, orientation=orientation)
            slider_object = settings(self, slider_object)
            for child in element:
                self.create_widget(slider_object, child)

        elif element.tag == "Switch":
            switch_object = tk.CTkSwitch(parent)
            switch_object = settings(self, switch_object)
            for child in element:
                self.create_widget(switch_object, child)

        elif element.tag == "TabView":
            tabview_object = tk.CTkTabview(parent)
            tabview_object = settings(self, tabview_object)
            for child in element:
                self.create_widget(tabview_object, child)

        elif element.tag == "Tab":
            if tab_text is not None:
                tab_object = parent.tab(tab_text)
                tab_object = settings(self, tab_object)
                for child in element:
                    self.create_widget(tab_object, child)

        elif element.tag == "TextArea":
            textbox_object = tk.CTkTextbox(parent)
            textbox_object = settings(self, textbox_object)
            for child in element:
                self.create_widget(textbox_object, child)

        elif element.tag == "Calender":
            from tkcalendar import Calendar
            # Calender Properties
            from datetime import datetime
            # Get current date and time
            current_datetime = datetime.now()
            # Extract year, month, and day from the current date
            current_year = current_datetime.year
            current_month = current_datetime.month
            current_day = current_datetime.day
            cursor = element.get('cursor') if element.get('cursor') is not None else ""
            year = element.get('year') if element.get('year') is not None else current_year
            month = element.get('month') if element.get('month') is not None else current_month
            day = element.get('day') if element.get('day') is not None else current_day

            # Add Calendar
            cal = Calendar(parent, selectmode='day',
                           year=int(year), month=int(month),
                           day=int(day), cursor=cursor)
            cal = settings(self, cal)
            for child in element:
                self.create_widget(cal, child)

        elif element.tag == 'TimePicker':
            from tktimepicker import AnalogPicker, AnalogThemes, constants
            time_formate = element.get('time_formate') if element.get('time_formate') is not None else constants.HOURS12
            if time_formate == "12":
                time_formate = constants.HOURS12
            elif time_formate == '24':
                time_formate = constants.HOURS24
            time_picker = AnalogPicker(parent, type=time_formate)
            theme = AnalogThemes(time_picker)
            _theme = element.get('theme') if element.get('theme') is not None else None
            if _theme == 'default':
                theme.setDracula()
            elif _theme == 'blue':
                theme.setNavyBlue()
            elif _theme == 'purple':
                theme.setPurple()
            time_picker = settings(self, time_picker)
            for child in element:
                self.create_widget(time_picker, child)

        elif element.tag == "PackPropagate":
            if flag is not None:
                parent.pack_propagate(flag=flag)

        elif element.tag == "Pack":
            if sticky is not None:
                parent.pack(sticky=sticky)
            if fill is not None:
                parent.pack(fill=fill)
            if anchor is not None:
                parent.pack(anchor=anchor)
            if padding_x is not None:
                parent.pack(padx=padding_x)
            if padding_y is not None:
                parent.pack(pady=padding_y)
            if expand is not None:
                parent.pack(expand=expand)
            if side is not None:
                parent.pack(side=side)
            if ipad_x is not None:
                parent.pack(ipadx=ipad_x)
            if ipad_y is not None:
                parent.pack(ipady=ipad_y)
            parent.pack()

        elif element.tag == "Grid":
            if grid_row is not None:
                parent.grid(row=int(grid_row))
            if grid_column is not None:
                parent.grid(column=int(grid_column))
            if grid_rowspan is not None:
                parent.grid(rowspan=int(grid_rowspan))
            if grid_columnspan is not None:
                parent.grid(columnspan=int(grid_columnspan))
            if sticky is not None:
                parent.grid(sticky=sticky)
            if anchor is not None:
                parent.grid(anchor=anchor)
            if padding_x is not None:
                parent.grid(padx=padding_x)
            if padding_y is not None:
                parent.grid(pady=padding_y)

        elif element.tag == 'GridRowConfigure':
            if grid_rowsconfig is not None:
                for i in [int(coord) for coord in grid_rowsconfig.strip('()').split(',')]:
                    parent.grid_rowconfigure(i, weight=int(grid_weight))
            if grid_rowconfig is not None:
                parent.grid_rowconfigure(int(grid_rowconfig), weight=int(grid_weight))

        elif element.tag == 'GridColumnConfigure':
            if grid_columnsconfig is not None:
                for i in [int(coord) for coord in grid_columnsconfig.strip('()').split(',')]:
                    parent.grid_columnconfigure(i, weight=int(grid_weight))
            if grid_columnconfig is not None:
                parent.grid_columnconfigure(int(grid_columnconfig), weight=int(grid_weight))

        else:
            if x is None or y is None:
                ValueError("Enter x and y value")
            elif x is None and y is not None:
                object.place(y=y)
            elif x is not None and y is None:
                object.place(x=x)
            else:
                object.place(x=x, y=y)
        pass

