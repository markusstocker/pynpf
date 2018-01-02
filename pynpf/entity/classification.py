from rdflib import Graph, Literal
from pynpf.vocab import SmartSMEAR
from rdflib.namespace import RDF, RDFS, XSD
from pynpf.entity.entity import Entity


class Classification(Entity):

    def __init__(self, identifier, label, comment):
        super().__init__(identifier)
        self.label = label
        self.comment = comment

    def get_label(self):
        return self.label

    def get_comment(self):
        return self.comment

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, SmartSMEAR.Classification))
        g.add((self.uri, RDFS.label, Literal(self.label, datatype=XSD.string)))
        g.add((self.uri, RDFS.comment, Literal(self.comment, datatype=XSD.string)))
        return g

