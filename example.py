import customtkinter as ctk
from CTkFloatingNotifications import NotificationManager, NotifyType

class Example(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Notification Example")
        self.notification_manager = NotificationManager(self)

        self.notify_button_info = ctk.CTkButton(self, text="Show Info", command=lambda: self.notification_manager.show_notification("This is an info notification!", NotifyType.INFO), fg_color="#00bfff", hover_color="#009acd")
        self.notify_button_info.pack(pady=10)
        
        self.notify_button_success = ctk.CTkButton(self, text="Show Success", command=lambda: self.notification_manager.show_notification("This is a success notification!", NotifyType.SUCCESS), fg_color="#28a745", hover_color="#218838")
        self.notify_button_success.pack(pady=10)
        
        self.notify_button_warning = ctk.CTkButton(self, text="Show Warning", command=lambda: self.notification_manager.show_notification("This is a warning notification!", NotifyType.WARNING), fg_color="#ffc107", hover_color="#e0a800")
        self.notify_button_warning.pack(pady=10)
        
        self.notify_button_error = ctk.CTkButton(self, text="Show Error", command=lambda: self.notification_manager.show_notification("This is an error notification!", NotifyType.ERROR), fg_color="#dc3545", hover_color="#c82333")
        self.notify_button_error.pack(pady=10)
        
        self.notify_button_error_dark = ctk.CTkButton(self, text="Show Error Dark", command=lambda: self.notification_manager.show_notification("This is an error notification!", NotifyType.ERROR, bg_color="#292929", text_color="#b0b0b0"), fg_color="#dc3545", hover_color="#c82333")
        self.notify_button_error_dark.pack(pady=10)

if __name__ == "__main__":
    app = Example()
    app.mainloop()
