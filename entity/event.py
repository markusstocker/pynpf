from hashlib import md5
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from entity.interval import Interval
from entity.instant import Instant
from entity.hyytiaelae import Hyytiaelae
from entity.point import Point
from vocab import LODE
from vocab import Base
from vocab import SmartSMEAR


class Event:
    def __init__(self, date='2011-03-26', place=Hyytiaelae()):
        self.date = date
        self.place = place
        self.space = Point(self.place.long, self.place.lat)
        self.time = None
        self.classification = None
        self.uri = URIRef('{}{}'.format(Base.ns,
                                        md5('{}{}'.format(self.date,
                                                          self.place.name)
                                            .encode())
                                        .hexdigest())
                          )

    def at_time(self, beginning, end):
        self.time = Interval(Instant(self.date, beginning), Instant(self.date, end))

    def event_class(self, classification):
        self.classification = classification

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, LODE.Event))
        g.add((self.uri, LODE.atPlace, self.place.uri))
        g.add((self.uri, LODE.atTime, self.time.uri))
        g.add((self.uri, LODE.inSpace, self.space.uri))
        g.add((self.uri, SmartSMEAR.hasEventClass, self.classification.uri))
        for s, p, o in self.place.graph():
            g.add((s, p, o))
        for s, p, o in self.time.graph():
            g.add((s, p, o))
        for s, p, o in self.space.graph():
            g.add((s, p, o))
        for s, p, o in self.classification.graph():
            g.add((s, p, o))
        return g
