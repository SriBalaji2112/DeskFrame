import sys
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
