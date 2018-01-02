from hashlib import md5
from rdflib import Graph
from rdflib.namespace import RDF
from pynpf.entity.interval import Interval
from pynpf.entity.instant import Instant
from pynpf.entity.point import Point
from pynpf.entity.entity import Entity
from pynpf.vocab import ENVO, LODE, Base, SmartSMEAR


class Process(Entity):
    def __init__(self, date=None, place=None):
        self.date = date
        self.place = place
        self.time = None
        self.geometry = None
        self.classification = None

        if date is not None and place is not None:
            super().__init__('{}{}'.format(Base.ns,
                                           md5('{}{}'.format(self.date, self.place.name).encode()).hexdigest()))

        if place is not None:
            self.set_in_space(Point(place.get_longitude(), place.get_latitude()))

    def set_time(self, beginning, end):
        self.time = Interval(Instant.from_date_time(self.date, beginning), Instant.from_date_time(self.date, end))

    def set_at_time(self, beginning, end):
        self.time = Interval(beginning, end)

    def get_at_time(self):
        return self.time

    def get_at_place(self):
        return self.place

    def set_at_place(self, place):
        self.place = place
        self.set_in_space(Point(place.get_longitude(), place.get_latitude()))

    def get_in_space(self):
        return self.geometry

    def set_in_space(self, geometry):
        self.geometry = geometry

    def set_classification(self, classification):
        self.classification = classification

    def get_classification(self):
        return self.classification

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, ENVO.ENVO_01001085))
        g.add((self.uri, RDF.type, ENVO.ENVO_02500003))
        g.add((self.uri, RDF.type, ENVO.ENVO_01001084))
        g.add((self.uri, RDF.type, ENVO.ENVO_02500000))
        g.add((self.uri, LODE.atPlace, self.place.uri))
        g.add((self.uri, LODE.inSpace, self.geometry.uri))
        g.add((self.uri, LODE.atTime, self.time.uri))
        g.add((self.uri, SmartSMEAR.hasClassification, self.classification.uri))
        for s, p, o in self.place.graph():
            g.add((s, p, o))
        for s, p, o in self.geometry.graph():
            g.add((s, p, o))
        for s, p, o in self.time.graph():
            g.add((s, p, o))
        for s, p, o in self.classification.graph():
            g.add((s, p, o))
        return g
