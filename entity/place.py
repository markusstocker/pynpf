from rdflib import Graph
from vocab import GeoNames
from vocab import DUL
from rdflib.namespace import RDF

class Place:

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, DUL.Place))
        g.add((self.uri, GeoNames.name, self.name))
        g.add((self.uri, GeoNames.countryCode, self.country_code))
        g.add((self.uri, GeoNames.locationMap, self.location_map))
        return g
