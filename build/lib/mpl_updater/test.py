import numpy as np
import matplotlib.pyplot as plt


def Animation(i, ax):
    ax.plot(np.arange(len(data)), data, c="red", label="Exakt")


data = [2, 1, 3, 0.13, 1, 20]


def Initialization():
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.35)
    return fig, ax
