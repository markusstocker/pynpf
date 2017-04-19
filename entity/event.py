from hashlib import md5
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from entity.interval import Interval
from entity.instant import Instant
from entity.hyytiaelae import Hyytiaelae
from entity.point import Point
from vocab import LODE
from vocab import Base


class Event:
    def __init__(self, date='2011-03-26', place=Hyytiaelae()):
        self.date = date
        self.place = place
        self.space = Point(self.place.long, self.place.lat)
        self.time = None
        self.involved = None
        self.uri = URIRef('{}{}'.format(Base.ns, md5(self.date.encode()).hexdigest()))

    def at_place(self, place):
        self.place = place

    def at_time(self, beginning, end):
        self.time = Interval(Instant(self.date, beginning), Instant(self.date, end))

    def get_place(self):
        return self.place

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, LODE.Event))
        g.add((self.uri, LODE.atPlace, self.place.uri))
        g.add((self.uri, LODE.atTime, self.time.uri))
        g.add((self.uri, LODE.inSpace, self.space.uri))
        for s, p, o in self.place.graph():
            g.add((s, p, o))
        for s, p, o in self.time.graph():
            g.add((s, p, o))
        for s, p, o in self.space.graph():
            g.add((s, p, o))
        return g
