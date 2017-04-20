from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from geomet import wkt


def mapevents(events):
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

    labels = list()
    longs = list()
    lats = list()

    for binding in events['results']['bindings']:
        labels.append(binding['placeName']['value'])
        point = wkt.loads(binding['spacePoint']['value'])
        coordinates = point['coordinates']
        longs.append(coordinates[0])
        lats.append(coordinates[1])

    x, y = m(longs, lats)
    m.plot(x, y, 'wo', markersize=12)

    for label, xpt, ypt in zip(labels, x, y):
        plt.text(xpt + 12000, ypt + 7000, label, color='white', weight='bold')

    plt.show()
