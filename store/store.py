import requests
import dateutil.parser
from datetime import datetime
from entity.event import Event
from entity.instant import Instant
from entity.place import Place
from vocab import SmartSMEAR
from entity.classification import Classification


class Store:

    query_base_path = 'query/resources'
    places = dict()
    classifications = dict()

    def __init__(self, endpoint='http://localhost:3030', dataset='pynpf'):
        self.endpoint = endpoint
        self.dataset = dataset
        self.url = '{}/{}'.format(endpoint, dataset)

        if not Store.places:
            self.load_places()

        if not Store.classifications:
            self.load_classifications()

    def query(self, query_string):
        return requests.post('{}/{}'.format(self.url, 'query'),
                             data={'query': query_string},
                             headers={'Accept': 'application/sparql-results+json'}).json()

    def load_places(self):
        response = self.query(open('{}/{}'.format(self.query_base_path, 'places.rq')).read())

        for binding in response['results']['bindings']:
            identifier = binding['placeUri']['value']
            name = binding['placeName']['value']
            country_code = binding['placeCountryCode']['value']
            location_map = binding['placeLocationMap']['value']
            latitude = binding['placeLatitude']['value']
            longitude = binding['placeLongitude']['value']
            Store.places[name] = Place(identifier, name, country_code, location_map, latitude, longitude)

    def load_classifications(self):
        response = self.query(open('{}/{}'.format(self.query_base_path, 'classifications.rq')).read())

        for binding in response['results']['bindings']:
            identifier = binding['classificationUri']['value']
            label = binding['classificationLabel']['value']
            comment = binding['classificationComment']['value']
            Store.classifications[label] = Classification(identifier, label, comment)

    @staticmethod
    def get_place(name):
        if name is None:
            return
        try:
            return Store.places[name]
        except LookupError:
            print('Place not found [name = {}]'.format(name))

    @staticmethod
    def get_classification(label):
        if label is None:
            return
        try:
            return Store.classifications[label]
        except LookupError:
            print('Classification not found [label = {}]'.format(label))

    def get_events(self, date=None, place=None):
        if date is not None and place is not None:
            date = datetime.strptime(date, '%Y-%m-%d')
            return self.eval_events(self.query(open('{}/{}'.format(self.query_base_path, 'events-filter-date-place.rq'))
                                               .read()
                                               .replace('PLACE_NAME', place.name)
                                               .replace('YEAR', str(date.year))
                                               .replace('MONTH', str(date.month))
                                               .replace('DAY', str(date.day))))

        if date is not None:
            date = datetime.strptime(date, '%Y-%m-%d')
            return self.eval_events(self.query(open('{}/{}'.format(self.query_base_path, 'events-filter-date.rq'))
                                               .read()
                                               .replace('YEAR', str(date.year))
                                               .replace('MONTH', str(date.month))
                                               .replace('DAY', str(date.day))))

        if place is not None:
            return self.eval_events(self.query(open('{}/{}'.format(self.query_base_path, 'events-filter-place.rq'))
                                               .read()
                                               .replace('PLACE_NAME', place.name)))

        return self.eval_events(self.query(open('{}/{}'.format(self.query_base_path, 'events-filter-none.rq'))
                                           .read()))

    @staticmethod
    def eval_events(response):
        events = list()

        for binding in response['results']['bindings']:
            beginning = dateutil.parser.parse(binding['beginningDateTime']['value'])
            end = dateutil.parser.parse(binding['endDateTime']['value'])
            place_name = binding['placeName']['value']
            classification_label = binding['classificationLabel']['value']
            event = Event(beginning.strftime('%Y-%m-%d'), Store.places[place_name])
            event.set_at_time(Instant(beginning), Instant(end))
            event.set_classification(Store.classifications[classification_label])
            events.append(event)

        return events

    def add_event(self, event):
        requests.post('{}/{}'.format(self.url, 'update'),
                      data={'update': 'INSERT DATA { ' + event.graph().serialize(format='nt').decode("utf-8") + ' }'},
                      headers={'Content-Type': 'application/x-www-form-urlencoded'})
