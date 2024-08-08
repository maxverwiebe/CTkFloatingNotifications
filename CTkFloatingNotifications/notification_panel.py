import customtkinter as ctk
import tkinter as tk
from .notification_type import NotifyType

class NotificationPanel(ctk.CTkFrame):
    def __init__(self, master, manager, message, notify_type=NotifyType.INFO, duration=5000, bg_color="#dbdbdb", text_color="#262626"):
        text_length = len(message)
        width = max(250, min(600, text_length * 7))  # Adjust the multiplier as needed
        height = 50

        super().__init__(master, corner_radius=0, fg_color=bg_color, width=width, height=height)
        self.pack_propagate(False)
        self.duration = duration
        self.manager = manager

        self.line_frame = ctk.CTkFrame(self, width=5, height=height, fg_color=notify_type.line_color)
        self.line_frame.place(relx=0, rely=0, anchor="nw")

        self.label = ctk.CTkLabel(self, text=message, text_color=text_color, anchor="w", font=("Arial", 12), justify="left")
        self.label.pack(pady=5, padx=(15, 10), fill="both", expand=True)

        self.close_button = ctk.CTkButton(self, text="✖", width=15, height=15, command=self.remove_notification, fg_color="transparent", hover_color=bg_color, text_color=text_color, corner_radius=10)
        self.close_button.place(relx=0.98, rely=0.1, anchor="ne")

        self.manager.add_notification(self)

        self.after(duration, self.remove_notification)

    def remove_notification(self):
        self.manager.remove_notification(self)
        self.destroy()