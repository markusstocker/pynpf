from hashlib import md5
from rdflib import Graph, Literal
from rdflib.namespace import RDF, XSD
from pynpf.entity.entity import Entity
from pynpf.vocab import Base, Time, OBI
from datetime import timedelta


class Duration(Entity):
    def __init__(self, duration=None):
        self.duration = duration
        self.numeric_duration = self.duration / timedelta(hours=1)

        if self.duration is not None:
            super().__init__('{}{}'.format(Base.ns,
                                           md5('{}'.format(self.duration.__hash__()).encode()).hexdigest()))

    def value(self):
        return self.duration

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, OBI.OBI_0001931))
        g.add((self.uri, RDF.type, Time.Duration))
        g.add((self.uri, Time.numericDuration, Literal(self.numeric_duration, datatype=XSD.decimal)))
        g.add((self.uri, Time.unitType, Time.unitHour))
        return g