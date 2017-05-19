import dateutil.parser
from rdflib.namespace import RDFS
from rdflib import Graph
from vocab import Time
from vocab import LODE
from vocab import GeoNames
from vocab import SmartSMEAR
from IPython.core.display import display, HTML


def describe(events, format='text'):

    if format == 'text':
        for event in events['results']['bindings']:
            beginning = dateutil.parser.parse(event['beginningDateTime']['value'])
            end = dateutil.parser.parse(event['endDateTime']['value'])
            print('A {} event occurred at {} ({}) [{}] on {} starting at {} and ending at {}.'
                  .format(event['classLabel']['value'],
                          event['placeName']['value'],
                          event['placeCountryCode']['value'],
                          event['placeLocationMap']['value'],
                          beginning.strftime('%Y-%m-%d'),
                          beginning.strftime('%H:%M'),
                          end.strftime('%H:%M')))
        return

    if format == 'rdf':
        g = Graph().parse(data=events, format='xml')
        print(g.serialize(format='n3', indent=4).decode('utf-8'))
        return

    raise ValueError('Unsupported format: {}'.format(format))
