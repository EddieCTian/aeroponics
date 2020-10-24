import config
import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, title, x_label, y_label, name):
        self.x=np.linspace(0, 12, int(12*60/float(config.SENSOR_UPDATE_TIME)+1))
        self.y=np.zeros(len(self.x))
        self.title=title
        self.x_label=x_label
        self.y_label=y_label
        self.name=name
    def add(self, new):
        self.y=np.insert(self.y, 0, new)
        self.y=np.delete(self.y, -1)
        return True
    def graph(self):
        plt.plot(self.x, self.y)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.savefig("graphs/"+self.name, bbox_inches='tight')
        return True
