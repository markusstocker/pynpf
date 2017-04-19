from hashlib import md5
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF
from vocab import Time, Base, SimpleFeatures, GeoSPARQL, Geo


class Point:
    def __init__(self, long, lat):
        self.point = 'POINT ({} {})'.format(long, lat)
        self.uri = URIRef('{}{}'.format(Base.ns, md5(self.point.encode()).hexdigest()))

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, SimpleFeatures.Point))
        g.add((self.uri, RDF.type, Geo.SpatialThing))
        g.add((self.uri, GeoSPARQL.asWKT, Literal(self.point, datatype=GeoSPARQL.wktLiteral)))
        return g
