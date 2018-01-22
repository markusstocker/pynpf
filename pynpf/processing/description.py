import io
import pydot
from IPython.display import display, Image, SVG
from rdflib import Graph
from pynpf.vocab import LODE, SmartSMEAR, WGS84, Time, SimpleFeatures
from pynpf.vocab import GeoSPARQL, GeoNames, DUL
from rdflib.tools.rdf2dot import rdf2dot


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

    if format == 'graph':
        rdflib_graph = Graph()
        rdflib_graph.bind('wgs84', WGS84.ns)
        rdflib_graph.bind('lode', LODE.ns)
        rdflib_graph.bind('time', Time.ns)
        rdflib_graph.bind('geosparql', GeoSPARQL.ns)
        rdflib_graph.bind('gn', GeoNames.ns)
        rdflib_graph.bind('sf', SimpleFeatures.ns)
        rdflib_graph.bind('DUL', DUL.ns)
        rdflib_graph.bind('smear', SmartSMEAR.ns)
        for event in events:
            for s, p, o in event.graph():
                rdflib_graph.add((s, p, o))
        stream = io.StringIO()
        rdf2dot(rdflib_graph, stream)
        (pydot_graph,) = pydot.graph_from_dot_data(stream.getvalue())
        display(SVG(pydot_graph.create_svg()))
        return


    raise ValueError('Unsupported format: {}'.format(format))
