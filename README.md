# CTkFloatingNotifications

CTkFloatingNotifications is a custom notification manager widget built using the CustomTkinter library. It provides an easy way to display various types of notifications within a CustomTkinter application, enhancing user experience with visual alerts.

![alt text](https://github.com/maxverwiebe/CTkFloatingNotifications/blob/main/preview.png?raw=true)

## Features

- **Information Notifications**: Display informational messages to the user.
- **Success Notifications**: Indicate successful operations.
- **Warning Notifications**: Alert users about potential issues.
- **Error Notifications**: Notify users about errors.
- **Dark Mode**: Display notifications with a dark background for better visibility in dark-themed applications.

## Installation

To use CTkFloatingNotifications, you need to have CustomTkinter and CTkFloatingNotifications installed.
```bash
pip install customtkinter
```

And clone this repo.

## Usage

### Basic Example

Here's a basic example of how to use CTkFloatingNotifications in your application:

```python
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
```

### Customization

- **Notification Colors**: Customize the foreground and hover colors for buttons to match your application's theme.
- **Dark Mode**: Use `bg_color` and `text_color` parameters to create dark-themed notifications.
- **Notification Duration**: Adjust the duration for which the notification is displayed using the `duration` parameter.

#### Example:

```python
self.notification_manager.show_notification(
    "This is a custom notification!",
    notify_type=NotifyType.INFO,
    duration=7000,  # Display for 7 seconds
    bg_color="#dbdbdb",  # Custom background color
    text_color="#262626"  # Custom text color
)
```

## Methods

### `show_notification(message, notify_type, bg_color=None, text_color=None)`

- **Description**: Display a notification with the specified message and type.
- **Parameters**: 
  - `message` (str): The message to display in the notification.
  - `notify_type` (NotifyType): The type of notification (INFO, SUCCESS, WARNING, ERROR).
  - `bg_color` (str, optional): Background color of the notification.
  - `text_color` (str, optional): Text color of the notification.

### Notification Types

- `NotifyType.INFO`: For informational messages.
- `NotifyType.SUCCESS`: For success messages.
- `NotifyType.WARNING`: For warning messages.
- `NotifyType.ERROR`: For error messages.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for providing a great framework for creating modern and customizable GUI applications in Python.

Feel free to customize this README to better suit your project's specific details and needs!
