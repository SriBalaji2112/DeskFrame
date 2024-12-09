import os
import sys
from tkinter import filedialog

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import customtkinter as tk
from deskframe.views.ViewBuilder import Builder
from PIL import Image
from deskframe.views.notification import Notification


class MainActivity(tk.CTkFrame):
    def __init__(self, master=None, intent=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.intent = intent
        self.view = Builder(context="activity_main.xml", _from=self)
        # Duration variables
        self.current_video = 0
        self.playlist_list = []
        self.current_duration = tk.StringVar()
        self.end_duration = tk.StringVar()
        self.progress_value = tk.IntVar(self)
        self.volume_label = tk.StringVar()
        self.current_duration.set(f"{self.format_time(0 / 1000)}")
        self.end_duration.set(f"{self.format_time(0 / 1000)}")

        self.app = self.view.getElementByID("video")
        self.start_time = self.view.getElementByID("start_time")
        self.end_time = self.view.getElementByID("end_time")
        self.progress_bar = self.view.getElementByID("progress_scale")
        self.play_btn = self.view.getElementByID("play_btn")
        self.skip_plus = self.view.getElementByID('skip_plus')
        self.skip_minus = self.view.getElementByID('skip_minus')
        self.volume_scale = self.view.getElementByID('volume_scale')
        self.volume_info = self.view.getElementByID('volume_info')
        self.menu_bar = self.view.getElementByID('menu_bar')
        self.next_btn = self.view.getElementByID('next_btn')
        self.prev_btn = self.view.getElementByID('prev_btn')
        self.pause_img_data = Image.open("./res/drawable/pause.png")
        self.pause_pg = tk.CTkImage(self.pause_img_data)
        self.play_img_data = Image.open("./res/drawable/play.png")
        self.play_pg = tk.CTkImage(self.play_img_data)
        self.onCreate()

    def onCreate(self):
        self.progress_bar.configure(from_=0, to=100,
                variable=tk.DoubleVar(), command=lambda value: self.skip_to_position(value, self.app.player))
        self.volume_scale.configure(from_=0, to=100,
                variable=tk.DoubleVar(), command=lambda value: self.set_volume(value, self.app.player))
        self.volume_scale.set(75)
        self.volume_label.set(f"Volume: {int(self.volume_scale.get())}%")
        self.volume_info.configure(textvariable=self.volume_label)
        self.after(10, lambda: self.update_duration_and_scale(self.app.player))
        self.play_btn.configure(command=lambda: self.play(self.app.player))
        self.start_time.configure(textvariable=self.current_duration)
        self.end_time.configure(textvariable=self.end_duration)
        self.next_btn.configure(command=lambda : self.play_next_video(self.app.player))
        self.prev_btn.configure(command=lambda : self.play_previous_video(self.app.player))
        self.skip_plus.configure(command=lambda : self.skip_seconds(5, self.app.player))
        self.skip_minus.configure(command=lambda: self.skip_seconds(-5, self.app.player))
        # self.skip_plus.configure(command=lambda: self.skip(5))
        self.menu_bar.add_command(label="Open File (ctlr+o)", command=self.openFile)
        self.menu_bar.add_command(label="Open Folder (ctlr+f)", command=self.open_folder)
        self.menu_bar.add_separator()
        self.menu_bar.add_command(label='Exit (ctlr+q)', command=lambda: self.master.quit())
        self.master.bind("<space>", lambda event: self.play(self.app.player))
        self.master.bind("<Next>", lambda event: self.play(self.app.player))
        self.master.bind("<Down>", lambda event: self.adjust_volume(-5, self.app.player))
        self.master.bind("<Up>", lambda event: self.adjust_volume(5, self.app.player))
        self.master.bind("<Right>", lambda event: self.skip_seconds(10, self.app.player))
        self.master.bind("<Left>", lambda event: self.skip_seconds(-10, self.app.player))
        self.master.bind("<Control-o>", lambda event: self.openFile())
        self.master.bind("<Control-f>", lambda event: self.open_folder())
        self.master.bind("<Control-p>", lambda event: self.playlist_window())
        self.master.bind("<Control-q>", lambda event: self.master.quit())
        pass

    # onClick Methods
    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            video_files = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".avi", ".mkv"))]
            video_paths = [os.path.join(folder_path, file) for file in video_files]
            self.playlist_list.extend(video_paths)
            self.app.load(self.playlist_list[0])
            self.title_notify(self.playlist_list[0])
            self.play(self.app.player)

    def play_next_video(self, player):
        # Play the next video in the playlist
        if self.playlist_list:
            if len(self.playlist_list) <= self.current_video:
                self.current_video = 0
            else:
                self.current_video += 1
            next_video_path = self.playlist_list[self.current_video]
            self.app.load(next_video_path)
            # player.play()
            self.title_notify(next_video_path)
            self.play(player)

    def play_previous_video(self, player):
        # Play the previous video in the playlist
        if self.playlist_list:
            if 0 == self.current_video:
                self.current_video = len(self.playlist_list)
            else:
                self.current_video -= 1
            last_video_path = self.playlist_list[self.current_video]
            self.app.load(last_video_path)
            self.title_notify(last_video_path)
            # player.play()
            self.play(player)

    def adjust_volume(self, delta, player):
        volume = player.audio_get_volume()
        volume += delta
        volume = max(0, min(100, volume))  # Ensure volume is within 0-100 range
        player.audio_set_volume(volume)

    def skip_seconds(self, seconds, player):
        current_time = player.get_time()
        if current_time != -1:
            target_time = max(0, current_time + (seconds * 1000))
            player.set_time(target_time)

    def update_duration_and_scale(self, player):
        if player.get_media():
            # Get current and end duration in milliseconds
            current_time = player.get_time()
            end_time = player.get_length()

            # Update the duration labels
            if current_time == -1:
                self.current_duration.set(f"{self.format_time(0 / 1000)}")
                self.end_duration.set(f"{self.format_time(0 / 1000)}")
            else:
                self.current_duration.set(f"{self.format_time(current_time / 1000)}")
                self.end_duration.set(f"{self.format_time(end_time / 1000)}")

            # Update the progress scale
            if end_time > 0:
                progress_percentage = (current_time / end_time) * 100
                self.progress_bar.set(progress_percentage)

            # Update the volume label
            self.volume_label.set(f"{int(player.audio_get_volume())}%")

        # Schedule the next update
        self.after(100, lambda: self.update_duration_and_scale(self.app.player))

    def format_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    def skip_to_position(self, value, player):
        if player.get_media():
            # Get the selected position from the progress scale
            selected_position = value

            # Calculate the corresponding time in milliseconds
            total_time = player.get_length()
            target_time = int((int(selected_position) / 100) * total_time)

            # Set the player's position to skip to the selected time
            player.set_time(target_time)

    def title_notify(self, file_path):
        video_name = os.path.basename(file_path)
        truncated_name = video_name[:50] + "..." if len(video_name) > 13 else video_name
        self.master.title(f"DeskFrame - {truncated_name}")
        Notification.notify(title=truncated_name,
                                 message="DeskFrame - Video and Audio Player : Now Playing",
                                 timeout=2)

    def openFile(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.mp3")])
        if file_path:
            self.app.load(file_path)
            self.play(self.app.player)
            self.update_duration_and_scale(self.app.player)
            self.playlist_list.append(file_path)
            self.title_notify(file_path)
            return file_path

    def play(self, player):
        if player.get_media() is None:
            # No video is loaded, open file dialog to select a video
            self.openFile()
            return
        if player.is_playing():
            self.play_btn.configure(image=self.play_pg)
            player.pause()
        else:
            self.play_btn.configure(image=self.pause_pg)
            player.play()
        # player.play()

    def pause(self, player):
        player.pause()

    def stop(self, player):
        player.stop()

    def set_volume(self, value, player):
        player.audio_set_volume(int(value))
        # Update the volume label
        self.volume_label.set(f"{int(player.audio_get_volume())}%")
    # User Define function

    def playlist_window(self):
        root = tk.CTkToplevel(self.master)
        root.attributes('-topmost', True)
        root.geometry('100x200')
        root.mainloop()

    # Switch View -> auto created InBuild method, please don't modify
    def Intent(self, view):
        if self.intent:
            self.pack_forget()               # Hide current window
            self.intent(view)  # Show destination window

