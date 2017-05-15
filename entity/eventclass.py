from rdflib import Graph
from vocab import SmartSMEAR
from rdflib.namespace import RDF
from rdflib.namespace import RDFS

class EventClass:

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, SmartSMEAR.EventClass))
        g.add((self.uri, RDFS.label, self.label))
        g.add((self.uri, RDFS.comment, self.comment))
        return g
