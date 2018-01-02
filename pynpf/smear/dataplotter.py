import numpy as np
from matplotlib import pyplot as plt


def plotdata(data):
    d = data.copy(deep=True)
    d = d.ix[:, 6:].as_matrix()
    m = len(d)
    n = len(d[0])
    x = range(0, m)
    y = range(0, n)
    x, y = np.meshgrid(x, y)
    z = np.transpose(np.array([row[1:] for row in d]).astype(np.float))
    plt.figure(figsize=(10, 5), dpi=100)
    plt.pcolormesh(x, y, z)
    plt.plot((0, x.max()), (y.max()/2, y.max()/2), "r-")
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
