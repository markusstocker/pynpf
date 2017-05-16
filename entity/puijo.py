from vocab import DUL
from vocab import GeoNames
from entity.place import Place
from rdflib.namespace import RDF, XSD
from rdflib import Graph, URIRef, Literal


class Puijo(Place):

    def __init__(self):
        self.uri = URIRef('http://sws.geonames.org/640784/')
        self.name = Literal('Puijo', datatype=XSD.string)
        self.country_code = Literal('FI', datatype=XSD.string)
        self.location_map = URIRef('http://www.geonames.org/640784/puijo.html')
        self.lat = 62.91667
        self.long = 27.65
        self.smear_table = 'PUI_dmps_tot'
        self.smear_variables = 'ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,' \
                               'ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32,' \
                               'ch33,ch34,ch35,ch36,ch37,ch38,ch39,ch40'
