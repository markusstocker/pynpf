from hashlib import md5
from rdflib.namespace import RDF, XSD
from rdflib import Graph, Literal, URIRef
from pytz import timezone
from datetime import datetime
from vocab import Time
from vocab import Base
import dateutil.parser
from entity.entity import Entity


class Instant(Entity):

    def __init__(self, datetime):
        self.datetime = datetime
        self.iso_datetime = self.datetime.isoformat()
        self.literal_datetime = Literal(self.iso_datetime, datatype=XSD.dateTime)
        super().__init__('{}{}'.format(Base.ns, md5(self.iso_datetime.encode()).hexdigest()))

    def get_datetime(self):
        return self.datetime

    def graph(self):
        g = Graph()
        g.add((self.uri, RDF.type, Time.Instant))
        g.add((self.uri, Time.inXSDDateTime, self.literal_datetime))
        return g

    @staticmethod
    def from_date_time(date, time, tz=timezone('Europe/Helsinki')):
        return Instant(tz.localize(datetime.strptime('{} {}'.format(date, time), '%Y-%m-%d %H:%M')))
