"""Main file for ArduinoFirmataManager
:author: B. Korzhak
:date: 06.05.2020
"""
from views import FirmataView


# Main flow for ArduinoFirmataManager
if __name__ == "__main__":
    view = FirmataView(winsize="840x480")
    view.window.mainloop()
