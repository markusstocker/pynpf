from kb.store import Store
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

m = Basemap(projection='merc',
            llcrnrlon=20.78,
            llcrnrlat=59.76,
            urcrnrlon=29.98,
            urcrnrlat=63.94,
            resolution='i')
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='#ddaa66', lake_color='#3535ff')
m.drawmapboundary(fill_color='#3535ff')

x, y = m([24.29077, 27.65], [61.84562, 62.91667])
m.plot(x, y, 'wo', markersize=12)

for label, xpt, ypt in zip(['Hyytiälä', 'Puijo'], x, y):
    plt.text(xpt+12000, ypt+7000, label, color='white', weight='bold')

plt.show()

# s = Store()
# events = s.get_events()

# print(events)
