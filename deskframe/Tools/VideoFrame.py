import tkinter as tk
import vlc
import platform

class VideoPlayerApp(tk.Frame):
    def __init__(self, master, filepath=''):
        super().__init__(master)
        # self.grid(row=0, column=0, sticky="nsew")

        # Create a VLC player instance
        self.Instance = vlc.Instance("--no-xlib")  # Use --no-xlib on Linux
        self.player = self.Instance.media_player_new()

        # Embed VLC player into Tkinter window
        if platform.system() == "Windows":
            self.player.set_hwnd(self.GetHandle())
        else:
            self.player.set_xwindow(self.GetHandle())

        # Set initial volume to 1/4 (25%)
        self.player.audio_set_volume(75)

    def load(self, filename):
        # Initialize with an empty media
        self.Media = self.Instance.media_new(filename)
        self.Media.get_mrl()
        self.player.set_media(self.Media)
        self.player.set_time(10)

    def GetHandle(self):
        # Get the window handle to embed the VLC player on Windows
        return self.winfo_id()
