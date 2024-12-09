import customtkinter as tk
from deskframe.views.rootBuilder import Builder
from Quiz.python.MainActivity import MainActivity
# 1100x580

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


if __name__ == "__main__":
    manager = WindowManager()
    manager.protocol("WM_DELETE_WINDOW", on_closing)
    manager.mainloop()
