import customtkinter as tk


class ToolBar(tk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Create a frame for the left buttons
        self.left_frame = tk.CTkFrame(self)
        self.left_frame.pack(side=tk.LEFT, anchor="n")

        # Create a frame for the right buttons
        self.right_frame = tk.CTkFrame(self)
        self.right_frame.pack(side=tk.RIGHT, anchor='n')
