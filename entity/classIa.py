from vocab import SmartSMEAR
from entity.eventclass import EventClass
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class ClassIa(EventClass):

    def __init__(self):
        self.uri = URIRef(SmartSMEAR.ClassIa)
        self.label = Literal('Class Ia', datatype=XSD.string)
        self.comment = Literal('Very clear and strong event', datatype=XSD.string)
