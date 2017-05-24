from vocab import GeoNames
from vocab import DUL
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal
from entity.entity import Entity


class Place(Entity):

    def __init__(self, identifier, name, country_code, location_map, latitude, longitude):
        super().__init__(identifier)
        self.name = name
        self.country_code = country_code
        self.location_map = location_map
        self.latitude = latitude
        self.longitude = longitude

    def get_name(self):
        return self.name

    def get_country_code(self):
        return self.country_code

    def get_location_map(self):
        return self.location_map

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude
