from hashlib import md5
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from pynpf.entity.interval import Interval
from pynpf.entity.instant import Instant
from pynpf.entity.point import Point
from pynpf.entity.entity import Entity
from pynpf.vocab import LODE, Base, SmartSMEAR, PROV


class Event(Entity):
    def __init__(self, date=None, place=None, prov=None):
        self.date = date
        self.place = place
        self.prov = prov
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
        g.add((self.uri, RDF.type, LODE.Event))
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

        g.add((self.uri, RDF.type, PROV.Entity))

        if self.prov is None:
            return g

        agent = None
        activity = None
        entity = None

        if 'agent' in self.prov:
            agent = URIRef(self.prov['agent'])
            g.add((agent, RDF.type, PROV.Agent))
            g.add((self.uri, PROV.wasAttributedTo, agent))

        if 'entity' in self.prov:
            entity = URIRef('file:{}'.format(self.prov['entity']))
            g.add((entity, RDF.type, PROV.Entity))
            g.add((self.uri, PROV.wasDerivedFrom, entity))

        if 'activity' in self.prov:
            activity = URIRef(self.prov['activity'])
            g.add((activity, RDF.type, PROV.Activity))
            g.add((self.uri, PROV.wasGeneratedBy, activity))

        if agent is not None and activity is not None:
            g.add((activity, PROV.wasAssociatedWith, agent))
        if activity is not None and entity is not None:
            g.add((activity, PROV.used, entity))

        return g
