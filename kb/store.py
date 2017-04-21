import requests
from datetime import datetime
from entity.hyytiaelae import Hyytiaelae


class Store:
    def __init__(self, endpoint='http://localhost:3030', dataset='pynpf'):
        self.url = '{}/{}'.format(endpoint, dataset)
        self.query_base_path = 'query/resources'

    def query(self, query, headers):
        return requests.post('{}/{}'.format(self.url, 'query'),
                             data={'query': query},
                             headers=headers)

    def get_events(self):
        return self.query(open('{}/{}'.format(self.query_base_path, 'select-events.rq')).read(),
                          {'Accept': 'application/sparql-results+json'}).json()

    def get_event(self, date='2011-03-26', place=Hyytiaelae()):
        date = datetime.strptime(date, '%Y-%m-%d')
        return self.query(open('{}/{}'.format(self.query_base_path, 'select-event.rq')).read()
                          .replace('PLACE_NAME', place.name.toPython())
                          .replace('YEAR', str(date.year))
                          .replace('MONTH', str(date.month))
                          .replace('DAY', str(date.day)),
                          {'Accept': 'application/rdf+xml'}).text

    def add_event(self, event):
        requests.post('{}/{}'.format(self.url, 'update'),
                      data={'update': 'INSERT DATA { ' + event.graph().serialize(format='nt').decode("utf-8") + ' }'},
                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
