import dateutil.parser
from rdflib import Graph
from vocab import Time
from vocab import LODE
from vocab import GeoNames
from IPython.core.display import display, HTML


def describe(event, format='text'):
    g = Graph().parse(data=event, format='xml')

    if format == 'text':
        beginningDateTime = dateutil.parser.parse(str(list(g[:Time.hasBeginning/Time.inXSDDateTime])[0][1].value))
        endDateTime = dateutil.parser.parse(str(list(g[:Time.hasEnd/Time.inXSDDateTime])[0][1].value))
        print('A new particle formation event occurred at {} ({}) [{}] on {} starting at {} and ending at {}.'
              .format(list(g[:LODE.atPlace/GeoNames.name])[0][1],
                      list(g[:LODE.atPlace/GeoNames.countryCode])[0][1],
                      list(g[:LODE.atPlace/GeoNames.locationMap])[0][1],
                      beginningDateTime.strftime('%Y-%m-%d'),
                      beginningDateTime.strftime('%H:%M'),
                      endDateTime.strftime('%H:%M')))
        return

    if format == 'rdf':
        print(g.serialize(format='n3', indent=4).decode('utf-8'))
        return

    raise ValueError('Unsupported format: {}'.format(format))
