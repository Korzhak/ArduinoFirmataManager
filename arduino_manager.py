import serial
import pyfirmata
import time


class ArduinoManager:
    def __init__(self):
        self.pin = 13
        self.port = "/dev/ttyUSB0"
        self.board = pyfirmata.Arduino(self.port)
        self.pin_state = {13: ""}
        it = pyfirmata.util.Iterator(self.board)
        it.start()
        self.analog_pin = {}

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

    def analog_init(self, analog_pin):
        self.analog_pin[analog_pin] = self.board.get_pin(f"a:{analog_pin}:i")

    def analog_read(self, analog_pin):
        return self.analog_pin[analog_pin].read()

    def blink(self):
        self.on_13_pin()
        time.sleep(2)
        self.off_13_pin()
        time.sleep(2)
