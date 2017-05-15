from vocab import SmartSMEAR
from entity.eventclass import EventClass
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class ClassIb(EventClass):

    def __init__(self):
        self.uri = URIRef(SmartSMEAR.ClassIb)
        self.label = Literal('Class Ib', datatype=XSD.string)
        self.comment = Literal('Unclear event', datatype=XSD.string)
