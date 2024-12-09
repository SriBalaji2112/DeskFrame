<h1 align="center">
  <b>D E S K F R A M E</b>
</h1>

<p align="center">
  DeskFrame is a Python library that simplifies the process of creating graphical user interfaces (GUIs) using XML for layout design and Python for backend logic.
</p>

<div align="center">

[![PyPI version](https://badge.fury.io/py/deskframe.svg)](https://badge.fury.io/py/deskframe) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/SriBalaji2112/DeskFrame/blob/main/LICENSE) ![Tkinter](https://img.shields.io/badge/Tkinter-latest_version-orange) ![CustomTkinter](https://img.shields.io/badge/CustomTkinter-latest_version-darkgreen)

</div>

## Introduction

**DeskFrame** is a Python library that simplifies the process of converting XML code into Python Tkinter applications. This module allows developers to design Tkinter interfaces using XML, ***providing a dynamic live preview*** of the Tkinter application as you write XML code.

The development of Tkinter applications by merging XML with Python.This module not only supports a vast array of standard and custom Tkinter widgets but elevates your development experience through its ***dynamic live preview feature***. 

As you frame your front-end piece in XML,instantly witness the changes reflecting in the live preview window.

This application supports the **toggling feature to enhance** user experience. The generated Tkinter code can be **easily converted into an executable file** with the help of our user-friendly DeskFrame tool.

## Features

### 1. Wide Widget Support

Support for all standard Tkinter and custom Tkinter widgets. Refer to the [documentation](https://github.com/YourUsername/YourRepository/blob/main/docs/widgets.md) for details on available widgets and their usage.

### 2. Live Preview

Once you run the project using `main.py`, all activities run dynamically, providing a simultaneous live preview. Any changes to the XML file are reflected immediately in the live preview window.

### 3. Front in XML

Design the front-end of your Tkinter application using XML.

### 4. Clean Separation

Maintain a clean separation between the front end and back end for better code organization and readability.

### 5. Customizable

Easily customize and fine-tune the generated Tkinter code, including support for custom widgets and layouts.

### 6. User-Friendly Project Structure

Utilize `deskframe.exe` in the site package to create projects effortlessly. Run `deskframe -startProject 'project_name'` in the command prompt. The project includes Python files for backend activities, XML files for layouts, and various resource folders for media, fonts, menus, and values.

### 7. Easy Application Creation

Use the provided `deskframe.exe` tool to streamline project setup, including creating new activities (`python setup.py -createActivity 'activity_name'`), running the DeskFrame server (`python setup.py -server run`), and more.

### 8. Build Executable File

Command: `python setup.py -buildExe`

## Examples with DeskFrame
#### DeskFrame Application - Start DeskFrame World
<center><img width='500px' src='deskframe/examples/images/sample.jpg'></center>

#### VLC Media - full fetched video player
<center><img width='500px' src='deskframe/examples/images/vlc.jpg'></center>

#### PyCharm-IDE - IDE UI
<center><img width='500px' src='deskframe/examples/images/PyCharm-IDE.jpg'></center>

#### CTk Demo App - CTk UI
<center><img width='500px' src='deskframe/examples/images/widgets.jpg'></center>

#### Login Window - Login UI with vertical align
<center><img width='500px' src='deskframe/examples/images/login-window.jpg'></center>

## Installation
#### You can install DeskFrame via pip:
Open a terminal or command prompt and run the following command:

```commandline
pip install deskframe
```

This will install DeskFrame and its dependencies on your system.

## Usage

### Create project:
Once DeskFrame is installed, you can create a new project by running the following command:

```commandline
deskframe --startProject project_name
```

Replace `project_name` with the desired name of your project. This command will create a new directory with the specified project name, containing the necessary files and folders to start developing your DeskFrame application.

In developing desktop applications with DeskFrame, organizing your project effectively is key to maintaining clarity and scalability. Let's explore the typical file structure of a DeskFrame project, providing a solid foundation for building your applications efficiently.

This guide provides an overview of the typical file structure you'll encounter after creating a DeskFrame project.

```
project_name/
    │
    ├── python/
    │ ├── MainActivity.py
    │ └── __init__.py
    │
    ├── res/
    │ ├── layout/
    │ │ └── activity_main.xml
    │ │
    │ ├── font/
    │ │ └── fonts.ttf
    │ │
    │ ├── drawable/
    │ │ ├── image1.png
    │ │ └── image2.jpg
    │ │
    │ ├── menu/
    │ │ └── main_menu.xml
    │ │
    │ └── values/
    │   ├── strings.py
    │   └── values.py
    │
    ├── builder.py
    ├── Config.xml
    ├── main.py
    ├── setup.py
    └── init.py
```


### Description of Each Component:

- **python/**: Contains the backend logic of your application. Each activity in your application has its corresponding Python file (e.g., `MainActivity.py`, `SecondActivity.py`).

- **res/**: Contains all the resources used in your application.

  - **layout/**: Contains XML files defining the UI layout of your activities.

  - **font/**: Contains font files (e.g., `.ttf`) used in your application.

  - **drawable/**: Contains image files (e.g., `.png`, `.jpg`) used in your application.

  - **menu/**: Contains XML files defining menus for your application.

  - **values/**: Contains configuration files (e.g., `strings.py`, `values.py`) holding constants and resource values.

- **builder.py**: Script to build the executable file for your project.

- **Config.xml**: Configuration file containing application settings and metadata.

- **main.py**: Main execution starting file of your application.

- **setup.py**: Script to create new activities and run the DeskFrame server.

- **\_\_init\_\_.py**: Python package initialization file.

This structured file organization ensures clarity, maintainability, and ease of development in your DeskFrame projects.


### XML script: `res\layout\activity_main.xml`

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Layout>
	<TextView
		text="Hello World">
		<Push
			expand="True"/>
	</TextView>
</Layout>
```

### Python Script: `python\MainActivity.py`

```python
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import customtkinter as tk
from deskframe.views.ViewBuilder import Builder

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
            self.pack_forget()               # Hide the current window
            self.intent(view)  # Show the destination window
```

### Output :
This script displays a Tkinter window with the centered text "Hello World."

### Creating an Activity in the Project :
To add a new activity to your DeskFrame project, you can use the provided command-line interface. Follow the steps below:
###### Command :
```commandline
~ cd project_directory
~ python setup.py --createActivity 'activity_name'
```
After running the command, DeskFrame will create the necessary files for the new activity, including Python backend and XML layout files, inside the appropriate directories (`python/` and `res/layout/`, respectively).

You can now start customizing your new activity by adding functionality to the Python
backend (`python/'ActivityName'.py`) and designing the UI layout in the XML file (`res/layout/'activity_name'.xml`).

### Run DeskFrame Live Server :
To live preview your DeskFrame project and make changes dynamically, you can run the DeskFrame live server using the provided command-line interface. Follow the instructions below:

```commandline
~ cd project_directory
~ python setup.py --server run
```
This command will launch the DeskFrame server, enabling live preview functionality. You can now make changes to your project files, such as Python scripts or XML layouts, and see the updates reflected immediately in the live preview.

To exit the live server, you can press `Ctrl + C` in the terminal or command prompt where the server is running.

### Run without Live Server
Alternatively, if you do not need live preview functionality and prefer to run your DeskFrame project without it, you can simply execute the main Python script (`main.py`) using the following command:

```
~ cd project_directory
~ python main.py
```

By following these steps, you can choose to either run the DeskFrame live server for dynamic previewing of your project or execute the main script directly for standard project execution.

# Supported Widgets
DeskFrame supports a wide range of widgets for building graphical user interfaces (GUIs) in Python applications. Below is a list of supported widgets along with links to their detailed documentation

Here's a brief overview of each supported widget in DeskFrame, along with a simple description:

```plaintext
+-------------------------+---------------------------------------------------------------+
|          Name           |                      Description                              |
+-------------------------+---------------------------------------------------------------+
| Frame                   | A container for organizing and grouping other widgets.        |
+-------------------------+---------------------------------------------------------------+
| ImageView               | Displays images or icons in your application.                 |
+-------------------------+---------------------------------------------------------------+
| TextView                | Displays text in your application.                            |
+-------------------------+---------------------------------------------------------------+
| Button                  | A clickable button that triggers actions. Supports various    |
|                         | attributes. Refer to the documentation for examples.          |
+-------------------------+---------------------------------------------------------------+
| CheckBox                | A checkable box that allows the user to make a binary choice. |
+-------------------------+---------------------------------------------------------------+
| WebCam                  | Placeholder for webcam-related functionality (customizable).  |
+-------------------------+---------------------------------------------------------------+
| Entry                   | Single-line text entry field.                                 |
+-------------------------+---------------------------------------------------------------+
| VideoView               | Displays video content in your application.                   |
+-------------------------+---------------------------------------------------------------+
| ListBox                 | A list of selectable items.                                   |
+-------------------------+---------------------------------------------------------------+
| MenuButton              | A button that opens a menu when clicked.                      |
+-------------------------+---------------------------------------------------------------+
| Menu                    | A popup menu for providing options and commands.              |
+-------------------------+---------------------------------------------------------------+
| Separator               | A visual separator used to organize layout.                   |
+-------------------------+---------------------------------------------------------------+
| ToolBar                 | A toolbar for quick access to frequently used actions.        |
+-------------------------+---------------------------------------------------------------+
| RadioButton             | A button that allows the user to choose one option from a set.|
+-------------------------+---------------------------------------------------------------+
| Scale                   | A slider that allows the user to select a value from a range. |
+-------------------------+---------------------------------------------------------------+
| LabeledScale            | A labeled slider for selecting a value from a range.          |
+-------------------------+---------------------------------------------------------------+
| Scrollbar               | A scrollbar for navigating content.                           |
+-------------------------+---------------------------------------------------------------+
| NoteBook                | A container for multiple pages with tabs for navigation.      |
+-------------------------+---------------------------------------------------------------+
| SpinBox                 | An input field for selecting numeric values from a range.     |
+-------------------------+---------------------------------------------------------------+
| TreeView                | A hierarchical way to display data in a tree-like structure.  |
+-------------------------+---------------------------------------------------------------+
| PanedFrame              | A container with resizable panes for flexible layout.         |
+-------------------------+---------------------------------------------------------------+
| ComboBox                | A combination of an entry and a dropdown list.                |
+-------------------------+---------------------------------------------------------------+
| OptionMenu              | A dropdown menu for selecting from a list of options.         |
+-------------------------+---------------------------------------------------------------+
| ProgressBar             | Visualizes the progression of an operation.                   |
+-------------------------+---------------------------------------------------------------+
| ScrollableFrame         | A frame with built-in scrolling capability.                   |
+-------------------------+---------------------------------------------------------------+
| SegmentedButton         | A set of buttons where only one can be selected at a time.    |
+-------------------------+---------------------------------------------------------------+
| Slider                  | Allows the user to select a value from a range using a slider.|
+-------------------------+---------------------------------------------------------------+
| Switch                  | A two-state toggle switch.                                    |
+-------------------------+---------------------------------------------------------------+
| TabView                 | Organizes content into tabs for easy navigation.              |
+-------------------------+---------------------------------------------------------------+
| TextArea                | A multi-line text entry field.                                |
+-------------------------+---------------------------------------------------------------+
| Calendar (DatePicker)   | Allows the user to pick a date from a calendar.               |
+-------------------------+---------------------------------------------------------------+
| TimePicker              | Allows the user to pick a time from a clock interface.        |
+-------------------------+---------------------------------------------------------------+
```


## Contact

If you have any questions, suggestions, or feedback regarding DeskFrame, we'd love to hear from you! You can reach out to us via the following channels:

- **Email**: [sribalaji2112@gmail.com](mailto:sribalaji2112@gmail.com) or [srij6838@gmail.com](mailto:srij6838@gmail.com)
- **Twitter**: [@DeskFrame](https://twitter.com/DeskFrameHQ)
- **LinkedIn**: [DeskFrame](https://www.linkedin.com/company/deskframe)

## Reporting Issues

If you encounter any issues while using DeskFrame, or if you have suggestions for improvements, please don't hesitate to report them on our GitHub Issues page. Your feedback helps us identify and address any problems in DeskFrame, ensuring a better experience for all users.

[Open a new issue](https://github.com/YourUsername/YourRepository/issues) on GitHub to report any bugs, request new features, or provide general feedback. We appreciate your contributions to improving DeskFrame!

## Authors

### Balaji Santhanam
![Balaji](https://example.com/john_doe_photo.jpg)

Balaji Santhanam is a software developer with expertise in Python and GUI development. He has contributed to the development of DeskFrame, focusing on widget implementation and user interface design.

### Jayasri
![Jayasri](https://example.com/jane_smith_photo.jpg)

Jayasri is a UI/UX designer with a passion for creating intuitive and visually appealing user interfaces. She has collaborated on the design and usability aspects of DeskFrame, ensuring a seamless user experience.

If you have any questions or need assistance with DeskFrame, feel free to reach out to Balaji or Jayasri via email at [sribalaji2112@gmail.com](mailto:sribalaji2112@gmail.com) or [srij6838@gmail.com](mailto:srij6838@gmail.com).

## Thank You for Visiting 🙏

Thank you for taking the time to visit and explore DeskFrame! We appreciate your interest in our project and hope that DeskFrame will be a valuable tool for your Python GUI development needs.

If you have any questions, feedback, or suggestions, please don't hesitate to reach out to us. We're here to support you in any way we can.

Happy coding with DeskFrame!