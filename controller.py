import csv
import time
from arduino_manager import ArduinoManager
from plot import Plot


class Controller:
    def __init__(self, filename:str="ReadData.csv", analog_pin:int=0):
        self.filename = filename
        self.am = ArduinoManager()
        self.am.analog_init(analog_pin)
        self.header = ['ID', 'VALUE']
        self.x = []
        self.y = []
        self.plot = Plot()

    def write_data(self):
        # time.sleep(3)
        print("Writing...")
        with open(self.filename, 'w') as f:
            w = csv.writer(f)
            w.writerow(self.header)
            i = 0
            while i < 25:
                time.sleep(0.5)
                data_from_arduino = self.am.analog_read(0)

                self.x.append(i)
                self.y.append(data_from_arduino)

                row = [i, data_from_arduino]
                w.writerow(row)
                i += 1
            return "Done."

    def draw_diagram(self):
        self.plot.write_plot(
            "Діаграма інтенсивності світла",
            self.header, self.x, self.y
        )