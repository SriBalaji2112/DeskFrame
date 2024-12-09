import customtkinter as tk
from tkinter import messagebox
import threading
import time
global window_width, window_height, x, y, target_y


class Toast:
    def __init__(self):
        self.LONGLENGTH = 4000
        self.SHORTLENGTH = 2000
        pass

    def move_toast(self):
        global toast, y
        while y > target_y:
            time.sleep(0.01)  # Adjust the sleep duration for smoother animation
            toast.geometry(f"{window_width}x{window_height}+{x}+{y}")
            y -= 2  # Adjust the step size for animation speed
        toast.geometry(f"{window_width}x{window_height}+{x}+{target_y}")

    def makeText(self, _from, message, waiting_time):
        global toast, x, y, target_y, window_width, window_height
        toast = tk.CTkToplevel(_from)
        toast.title("Toast Message")
        toast.overrideredirect(True)  # Hide the window frame

        # Get the screen width and height
        screen_width = _from.winfo_screenwidth()
        screen_height = _from.winfo_screenheight()

        # Calculate the width based on the length of the message
        window_width = len(message) * 10  # Adjust the factor based on your preference

        # Get the window height
        window_height = 30  # You can adjust this height based on your content

        # Calculate the bottom center point
        x = (screen_width - window_width) // 2
        x += 200
        y = screen_height+50  # Start off the screen

        target_y = screen_height - window_height - 10  # Adjust 10 as needed for spacing from the bottom
        target_y += 70
        toast.geometry(f"{window_width}x{window_height}+{x}+{y}")

        label = tk.CTkLabel(toast, text=message)
        label.pack()

        # Create a thread to move the toast window
        threading.Thread(target=self.move_toast).start()

        toast.after(waiting_time, self.close_toast)  # 2000 milliseconds (2 seconds) delay

    def close_toast(self):
        toast.destroy()

