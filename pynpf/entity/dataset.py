from hashlib import md5
from rdflib import Graph, Literal, BNode
from rdflib.namespace import RDF, XSD
from pynpf.entity.entity import Entity
from pynpf.vocab import Base, Time, IAO, BFO


class DataSet(Entity):
    def __init__(self, events=None):
        self.events = events

        if self.events is not None:
            super().__init__('{}{}'.format(Base.ns,
                                           md5('{}'.format(self.events.__hash__()).encode()).hexdigest()))

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, IAO.IAO_0000100))

        for event in self.events:
            g.add((self.uri. BFO.BFO_0000051, event.uri))

        return g