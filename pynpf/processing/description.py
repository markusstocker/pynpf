from rdflib import Graph
from pynpf.vocab import LODE, SmartSMEAR, WGS84, Time, SimpleFeatures
from pynpf.vocab import GeoSPARQL, GeoNames, DUL


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
        g.bind('wgs84', WGS84.ns)
        g.bind('lode', LODE.ns)
        g.bind('time', Time.ns)
        g.bind('geosparql', GeoSPARQL.ns)
        g.bind('gn', GeoNames.ns)
        g.bind('sf', SimpleFeatures.ns)
        g.bind('DUL', DUL.ns)
        g.bind('smear', SmartSMEAR.ns)
        for event in events:
            for s, p, o in event.graph():
                g.add((s, p, o))
        print(g.serialize(format='turtle', indent=4).decode('utf-8'))
        return

    raise ValueError('Unsupported format: {}'.format(format))
