import requests


class Store:
    def __init__(self, endpoint='http://localhost:3030', dataset='pynpf'):
        self.endpoint = endpoint
        self.dataset = dataset
        self.headers = {'Accept': 'application/sparql-results+json'}
        self.query = None
        self.query_string = None
        self.data = None

    def query(self, query):
        self.query = query
        self.query_string = self.query.get_query()
        self.data = {'query': self.query_string}
        return requests.post(self.url, data=self.data, headers=self.headers).json()

    def add_event(self, event):
        url = self.endpoint + '/' + self.dataset + '/update'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'update': 'INSERT DATA { ' + event.graph().serialize(format='nt').decode("utf-8") + ' }'}
        requests.post(url, data=data, headers=headers)
