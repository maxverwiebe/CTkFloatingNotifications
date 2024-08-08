from enum import Enum

class NotifyType(Enum):
    INFO = ("#00bfff")  # Dark gray with blue line
    SUCCESS = ("#28a745")  # Dark gray with green line
    WARNING = ("#ffc107")  # Dark gray with orange line
    ERROR = ("#dc3545")  # Dark gray with red line

    def __init__(self, line_color):
        self.line_color = line_color