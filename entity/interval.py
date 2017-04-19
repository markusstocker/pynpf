from hashlib import md5
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, XSD
from vocab import Time, Base


class Interval:
    def __init__(self, beginning, end):
        self.beginning = beginning
        self.end = end
        self.iso_interval = '{}/{}'.format(beginning.iso_datetime, end.iso_datetime)
        self.uri = URIRef('{}{}'.format(Base.ns, md5(self.iso_interval.encode()).hexdigest()))

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
