from rdflib import Graph


def select(data):
    return Graph().parse(data=data, format='xml').query(
        open('{}/{}'.format('query/resources', 'select-events-filter-none.rq')).read()
    )


