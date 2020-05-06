from arduino_manager import ArduinoManager
from views import FirmataView


if __name__ == "__main__":
    view = FirmataView()
    view.window.mainloop()
    # am = ArduinoManager()
    # for i in range(10):
    #     am.blink()