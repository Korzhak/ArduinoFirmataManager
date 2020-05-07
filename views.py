from tkinter import *
from controller import Controller
from PIL import Image, ImageTk


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
        self.controller = Controller()

    def clicked(self):
        if not self.controller.am.pin_state[13]:
            self.controller.am.on_13_pin()
        else:
            if self.controller.am.pin_state[13] == 'HIGH':
                self.controller.am.off_13_pin()
            else:
                self.controller.am.on_13_pin()

        self.lbl1.configure(text=f"13 pin state: {self.controller.am.pin_state[13]}")

    def read_data(self):
        self.lbl2.configure(text=self.controller.write_data())

        img = ImageTk.PhotoImage(Image.open("plot.png"))
        lbl_img = Label(image=img)
        lbl_img.image = img  # keep a reference!
        lbl_img.grid(column=3, row=0)

    def _add_label(self, label_text):
        self.lbl1 = Label(self.window, text=label_text)
        self.lbl1.grid(column=0, row=0)
        self.lbl2 = Label(self.window, text="Read data from Arduino")
        self.lbl2.grid(column=0, row=1)

    def _add_button(self, button_text):
        btn1 = Button(self.window, text=button_text, command=self.clicked)
        btn1.grid(column=1, row=0)
        btn2 = Button(self.window, text="Read", command=self.read_data)
        btn2.grid(column=1, row=1)
