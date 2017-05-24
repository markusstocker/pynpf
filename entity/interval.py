from hashlib import md5
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, XSD
from vocab import Time, Base
from entity.entity import Entity


class Interval(Entity):
    def __init__(self, beginning, end):
        self.beginning = beginning
        self.end = end
        self.iso_interval = '{}/{}'.format(beginning.iso_datetime, end.iso_datetime)
        super().__init__('{}{}'.format(Base.ns, md5(self.iso_interval.encode()).hexdigest()))

    def get_beginning(self):
        return self.beginning

    def get_end(self):
        return self.end

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, Time.Interval))
        g.add((self.uri, Time.hasBeginning, self.beginning.uri))
        g.add((self.uri, Time.hasEnd, self.end.uri))
        for s, p, o in self.beginning.graph():
            g.add((s, p, o))
        for s, p, o in self.end.graph():
            g.add((s, p, o))
        return g
