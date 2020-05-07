from matplotlib import pyplot


class Plot:
    def __init__(self):
        pass

    def write_plot(self, title:str, headers:list, x:list, y:list):
        f = pyplot.figure()
        pyplot.plot(x, y, '-')
        pyplot.title(title)
        pyplot.xlabel(headers[0])
        pyplot.ylabel(headers[1])
        pyplot.savefig("plot.png")
