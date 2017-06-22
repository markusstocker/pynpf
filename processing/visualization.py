from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from geomet import wkt
from ipyleaflet import Map, Marker
from math import pi, cos, sin, atan2, sqrt


def centroid(coords):
    x = [p[0] for p in coords]
    y = [p[1] for p in coords]
    centroid = (sum(x) / len(coords), sum(y) / len(coords))

    return centroid


def imap(events):
    labels = list()
    coords = list()

    for event in events:
        labels.append(event.get_at_place().get_name())
        point = wkt.loads(event.get_in_space().get_wkt())
        coord = point['coordinates']
        coords.append([coord[0], coord[1]])

    c = centroid(coords)
    m = Map(center=[c[1], c[0]], zoom=4)

    for index, coord in enumerate(coords):
        mark = Marker(location=[coord[1], coord[0]], title=labels[index])
        mark.visible
        m += mark

    return m


def smap(events):
    plt.figure(figsize=(10, 5), dpi=150)
    m = Basemap(projection='merc',
                llcrnrlon=20.78,
                llcrnrlat=59.76,
                urcrnrlon=31.98,
                urcrnrlat=69.94,
                resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    m.fillcontinents(color='#ddaa66', lake_color='#3535ff')
    m.drawmapboundary(fill_color='#3535ff')

    labels = list()
    longs = list()
    lats = list()

    for event in events:
        labels.append(event.get_at_place().get_name())
        point = wkt.loads(event.get_in_space().get_wkt())
        coordinates = point['coordinates']
        longs.append(coordinates[0])
        lats.append(coordinates[1])

    x, y = m(longs, lats)
    m.plot(x, y, 'wo', markersize=12)

    for label, xpt, ypt in zip(labels, x, y):
        plt.text(xpt + 12000, ypt + 7000, label, color='white', weight='bold')

    plt.show()
