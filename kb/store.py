import requests


class Store:
    def __init__(self, endpoint='http://localhost:3030', dataset='pynpf'):
        self.url = '{}/{}'.format(endpoint, dataset)
        self.query_base_path = '../query/resources'

    def query(self, query):
        return requests.post('{}/{}'.format(self.url, 'query'),
                             data={'query': query},
                             headers={'Accept': 'application/sparql-results+json'}).json()

    def get_events(self):
        return self.query(open('{}/{}'.format(self.query_base_path, 'select-events.rq')).read())

    def add_event(self, event):
        requests.post('{}/{}'.format(self.url, 'update'),
                      data={'update': 'INSERT DATA { ' + event.graph().serialize(format='nt').decode("utf-8") + ' }'},
                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
