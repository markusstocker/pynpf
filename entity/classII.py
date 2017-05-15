from vocab import SmartSMEAR
from entity.eventclass import EventClass
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class ClassII(EventClass):

    def __init__(self):
        self.uri = URIRef(SmartSMEAR.ClassII)
        self.label = Literal('Class II', datatype=XSD.string)
        self.comment = Literal('Event with little confidence level', datatype=XSD.string)
