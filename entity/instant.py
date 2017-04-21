from hashlib import md5
from rdflib.namespace import RDF, XSD
from rdflib import Graph, Literal, URIRef
from pytz import timezone
from datetime import datetime
from vocab import Time
from vocab import Base


class Instant:
    def __init__(self, date, time, tz=timezone('Europe/Helsinki')):
        self.date = date
        self.time = time
        self.datetime = datetime.strptime('{} {}'.format(date, time), '%Y-%m-%d %H:%M')
        self.localized_datetime = tz.localize(self.datetime)
        self.iso_datetime = self.localized_datetime.isoformat()
        self.literal_datetime = Literal(self.iso_datetime, datatype=XSD.dateTime)
        self.uri = URIRef('{}{}'.format(Base.ns, md5(self.iso_datetime.encode()).hexdigest()))

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, Time.Instant))
        g.add((self.uri, Time.inXSDDateTime, self.literal_datetime))
        return g
