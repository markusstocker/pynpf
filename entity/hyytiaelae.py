from vocab import DUL
from vocab import GeoNames
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class Hyytiaelae:
    def __init__(self):
        self.uri = URIRef('http://sws.geonames.org/656888/')
        self.name = Literal('Hyytiälä', datatype=XSD.string)
        self.country_code = Literal('FI', datatype=XSD.string)
        self.location_map = URIRef('http://www.geonames.org/656888/hyytiaelae.html')
        self.lat = 61.84562
        self.long = 24.29077

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, DUL.Place))
        g.add((self.uri, GeoNames.name, self.name))
        g.add((self.uri, GeoNames.countryCode, self.country_code))
        g.add((self.uri, GeoNames.locationMap, self.location_map))
        return g
