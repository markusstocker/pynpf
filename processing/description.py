from rdflib import Graph
from vocab import LODE, Base, SmartSMEAR, WGS84, Time, GeoSPARQL, GeoNames, SimpleFeatures, DUL
from rdflib.namespace import NamespaceManager


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
        manager = NamespaceManager(Graph())
        manager.bind('wgs84', WGS84.ns)
        manager.bind('lode', LODE.ns)
        manager.bind('time', Time.ns)
        manager.bind('geosparql', GeoSPARQL.ns)
        manager.bind('smear', SmartSMEAR.ns)
        manager.bind('gn', GeoNames.ns)
        manager.bind('sf', SimpleFeatures.ns)
        manager.bind('DUL', DUL.ns)
        manager.bind('', Base.ns)
        g = Graph(namespace_manager=manager)
        for event in events:
            for s, p, o in event.graph():
                g.add((s, p, o))
        print(g.serialize(format='n3', indent=4).decode('utf-8'))
        return

    raise ValueError('Unsupported format: {}'.format(format))
