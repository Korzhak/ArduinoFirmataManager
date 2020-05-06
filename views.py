from tkinter import *
from arduino_manager import ArduinoManager

class FirmataView:
    def __init__(
            self, title:str="Firmata App",
            winsize:str="350x200",
            label_text:str="Push button",
            button_text:str="Take 13 pin"
    ):
        # main config
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(winsize)

        # add label and button
        self._add_label(label_text)
        self._add_button(button_text)

        # working with Arduino by manager
        self.arduino_manager = ArduinoManager()

    def clicked(self):
        if not self.arduino_manager.pin_state[13]:
            self.arduino_manager.on_13_pin()
        else:
            if self.arduino_manager.pin_state[13] == 'HIGH':
                self.arduino_manager.off_13_pin()
            else:
                self.arduino_manager.on_13_pin()

        self.lbl.configure(text=f"13 pin state: {self.arduino_manager.pin_state[13]}")

    def _add_label(self, label_text):
        self.lbl = Label(self.window, text=label_text)
        self.lbl.grid(column=0, row=0)

    def _add_button(self, button_text):
        btn = Button(self.window, text=button_text, command=self.clicked)
        btn.grid(column=1, row=0)

