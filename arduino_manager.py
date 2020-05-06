import serial
import pyfirmata
import time


class ArduinoManager:
    def __init__(self):
        self.pin = 13
        self.port = "/dev/ttyUSB0"
        self.board = pyfirmata.Arduino(self.port)
        self.pin_state = {13: ""}

    def on_pin(self, pin_numb: int):
        self.board.digital[pin_numb].write(1)
        self.pin_state[pin_numb] = "HIGH"

    def off_pin(self, pin_numb: int):
        self.board.digital[pin_numb].write(0)
        self.pin_state[pin_numb] = "LOW"

    def on_13_pin(self):
        self.board.digital[self.pin].write(1)
        self.pin_state[13] = "HIGH"

    def off_13_pin(self):
        self.board.digital[self.pin].write(0)
        self.pin_state[13] = "LOW"

    def blink(self):
        self.on_13_pin()
        time.sleep(2)
        self.off_13_pin()
        time.sleep(2)

