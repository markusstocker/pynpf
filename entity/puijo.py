from vocab import DUL
from vocab import GeoNames
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class Puijo:
    def __init__(self):
        self.uri = URIRef('http://sws.geonames.org/640784/')
        self.name = Literal('Puijo', datatype=XSD.string)
        self.country_code = Literal('FI', datatype=XSD.string)
        self.location_map = URIRef('http://www.geonames.org/640784/puijo.html')
        self.lat = 62.91667
        self.long = 27.65

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, DUL.Place))
        g.add((self.uri, GeoNames.name, self.name))
        g.add((self.uri, GeoNames.countryCode, self.country_code))
        g.add((self.uri, GeoNames.locationMap, self.location_map))
        return g
