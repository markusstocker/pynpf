import numpy as np
from matplotlib import pyplot as plt


def plotdata(data_set):
    del data_set[0] # Remove header
    for row in data_set: # Remove datetime data
        del row[0:6]
    m = len(data_set)
    n = len(data_set[0])
    x = range(0, m)
    y = range(0, n)
    x, y = np.meshgrid(x, y)
    z = np.transpose(np.array([row[1:] for row in data_set]).astype(np.float))
    plt.figure(figsize=(10, 5))
    plt.pcolormesh(x, y, z)
    plt.colorbar()
    plt.xlim(xmax=m-1)
    x_ticks = np.arange(x.min(), x.max(), 6)
    x_labels = range(x_ticks.size)
    plt.xticks(x_ticks, x_labels)
    plt.xlabel('Hours')
    y_ticks = np.arange(y.min(), y.max(), 6)
    y_labels = ['3.16', '6.31', '12.6', '25.1', '50.1', '100']
    plt.yticks(y_ticks, y_labels)
    plt.ylabel('Diameter [nm]')
    plt.ylim(ymax=n-1)
    plt.show()
