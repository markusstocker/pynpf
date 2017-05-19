import requests
from datetime import datetime
from entity.hyytiaelae import Hyytiaelae


class Store:
    def __init__(self, endpoint='http://localhost:3030', dataset='pynpf'):
        self.url = '{}/{}'.format(endpoint, dataset)
        self.query_base_path = 'query/resources'

    def query(self, query, accept):
        return requests.post('{}/{}'.format(self.url, 'query'),
                             data={'query': query},
                             headers={'Accept': accept})

    def get_events(self, date=None, place=None, query='select'):
        accept = 'application/sparql-results+json' if query == 'select' else 'application/rdf+xml'

        if date is None and place is None:
            rs = self.query(open('{}/{}-{}'.format(self.query_base_path, query, 'events-filter-none.rq')).read(),accept)
        elif date is not None:
            date = datetime.strptime(date, '%Y-%m-%d')
            rs = self.query(open('{}/{}-{}'.format(self.query_base_path, query, 'events-filter-date.rq')).read()
                            .replace('YEAR', str(date.year))
                            .replace('MONTH', str(date.month))
                            .replace('DAY', str(date.day)),
                            accept)
        elif place is not None:
            rs = self.query(open('{}/{}-{}'.format(self.query_base_path, query, 'events-filter-place.rq')).read()
                            .replace('PLACE_NAME', place.name.toPython()),
                            accept)
        else:
            date = datetime.strptime(date, '%Y-%m-%d')
            rs = self.query(open('{}/{}-{}'.format(self.query_base_path, query, 'events-filter-date-place.rq')).read()
                            .replace('PLACE_NAME', place.name.toPython())
                            .replace('YEAR', str(date.year))
                            .replace('MONTH', str(date.month))
                            .replace('DAY', str(date.day)),
                            accept)

        if query == 'select':
            return rs.json()

        return rs.text

    def add_event(self, event):
        requests.post('{}/{}'.format(self.url, 'update'),
                      data={'update': 'INSERT DATA { ' + event.graph().serialize(format='nt').decode("utf-8") + ' }'},
                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
