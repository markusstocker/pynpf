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
        for event in events:
            attime = event.get_at_time()
            beginning = attime.get_beginning()
            end = attime.get_end()
            place = event.get_at_place()
            print('A {} event occurred at {} ({}) [{}] on {} starting at {} and ending at {}.'
                  .format(event.get_classification().label,
                          place.get_name(),
                          place.get_country_code(),
                          place.get_location_map(),
                          beginning.get_datetime().strftime('%Y-%m-%d'),
                          beginning.get_datetime().strftime('%H:%M'),
                          end.get_datetime().strftime('%H:%M')))
        return

    if format == 'rdf':
        g = Graph()
        for event in events:
            for s, p, o in event.graph():
                g.add((s, p, o))
        print(g.serialize(format='n3', indent=4).decode('utf-8'))
        return

    raise ValueError('Unsupported format: {}'.format(format))
