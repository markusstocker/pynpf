from vocab import GeoNames
from entity.place import Place
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class Vaerrioe(Place):

    def __init__(self):
        self.uri = URIRef('http://sws.geonames.org/828747/')
        self.name = Literal('Värriö', datatype=XSD.string)
        self.country_code = Literal('FI', datatype=XSD.string)
        self.location_map = URIRef('http://www.geonames.org/828747/vaerrioe.html')
        self.lat = 67.46535
        self.long = 27.99231
        self.smear_table = 'VAR_DMPS'
        self.smear_variables = 'd316e1,d355e1,d398e1,d447e1,d501e1,d562e1,d631e1,d708e1,d794e1,' \
                'd891e1,d100e2,d112e2,d126e2,d141e2,d158e2,d178e2,d200e2,d224e2,' \
                'd251e2,d282e2,d316e2,d355e2,d398e2,d447e2,d501e2,d562e2,d631e2,' \
                'd708e2,d794e2,d891e2,d100e3,d112e3,d126e3,d141e3,d158e3,d178e3,d200e3'
