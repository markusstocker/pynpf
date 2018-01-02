import requests
import dateutil.parser
from datetime import datetime
from pynpf.entity.event import Event
from pynpf.entity.instant import Instant
from pynpf.entity.place import Place
from pynpf.entity.classification import Classification


class Store:

    places = dict()
    classifications = dict()

    places_query = '''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX wgs: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>

SELECT ?placeUri ?placeName ?placeCountryCode ?placeLocationMap ?placeLatitude ?placeLongitude
WHERE
{
  ?placeUri rdf:type dul:Place .
  ?placeUri gn:name ?placeName .
  ?placeUri gn:countryCode ?placeCountryCode .
  ?placeUri gn:locationMap ?placeLocationMap .
  ?placeUri wgs:lat ?placeLatitude .
  ?placeUri wgs:long ?placeLongitude .
}'''

    classifications_query = '''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX smear: <http://avaa.tdata.fi/web/smart/smear/>

SELECT ?classificationUri ?classificationLabel ?classificationComment
WHERE
{
  ?classificationUri rdf:type smear:Classification .
  ?classificationUri rdfs:label ?classificationLabel .
  ?classificationUri rdfs:comment ?classificationComment .
}'''

    events_filter_date_place_query = '''PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX lode: <http://linkedevents.org/ontology/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX sf: <http://www.opengis.net/ont/sf#>
PREFIX geosparql: <http://www.opengis.net/ont/geosparql#>
PREFIX smear: <http://avaa.tdata.fi/web/smart/smear/>

SELECT ?eventUri ?timeUri ?beginningUri ?beginningDateTime
  ?endUri ?endDateTime ?placeUri ?placeName ?placeCountryCode ?placeLocationMap
  ?spaceUri ?spacePoint ?classificationUri ?classificationLabel
WHERE
{
  ?eventUri rdf:type lode:Event .
  ?eventUri lode:atTime ?timeUri .
  ?timeUri rdf:type time:Interval .
  ?timeUri time:hasBeginning ?beginningUri .
  ?beginningUri rdf:type time:Instant .
  ?beginningUri time:inXSDDateTime ?beginningDateTime .
  ?timeUri time:hasEnd ?endUri .
  ?endUri rdf:type time:Instant .
  ?endUri time:inXSDDateTime ?endDateTime .
  ?eventUri lode:atPlace ?placeUri .
  ?placeUri rdf:type dul:Place .
  ?placeUri gn:name ?placeName .
  ?placeUri gn:countryCode ?placeCountryCode .
  ?placeUri gn:locationMap ?placeLocationMap .
  ?eventUri lode:inSpace ?spaceUri .
  ?spaceUri rdf:type sf:Point .
  ?spaceUri geosparql:asWKT ?spacePoint .
  ?eventUri smear:hasClassification ?classificationUri .
  ?classificationUri rdfs:label ?classificationLabel .

  FILTER (?placeName = "PLACE_NAME"^^xsd:string)
  FILTER (year(?beginningDateTime) = YEAR
    && month(?beginningDateTime) = MONTH
    && day(?beginningDateTime) = DAY)
}'''

    events_filter_date_query = '''PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX lode: <http://linkedevents.org/ontology/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX sf: <http://www.opengis.net/ont/sf#>
PREFIX geosparql: <http://www.opengis.net/ont/geosparql#>
PREFIX smear: <http://avaa.tdata.fi/web/smart/smear/>

SELECT ?eventUri ?intervalUri ?beginningUri ?beginningDateTime
  ?endUri ?endDateTime ?placeUri ?placeName ?placeCountryCode ?placeLocationMap
  ?spaceUri ?spacePoint ?classificationUri ?classificationLabel
WHERE
{
  ?eventUri rdf:type lode:Event .
  ?eventUri lode:atTime ?intervalUri .
  ?intervalUri rdf:type time:Interval .
  ?intervalUri time:hasBeginning ?beginningUri .
  ?beginningUri rdf:type time:Instant .
  ?beginningUri time:inXSDDateTime ?beginningDateTime .
  ?intervalUri time:hasEnd ?endUri .
  ?endUri rdf:type time:Instant .
  ?endUri time:inXSDDateTime ?endDateTime .
  ?eventUri lode:atPlace ?placeUri .
  ?placeUri rdf:type dul:Place .
  ?placeUri gn:name ?placeName .
  ?placeUri gn:countryCode ?placeCountryCode .
  ?placeUri gn:locationMap ?placeLocationMap .
  ?eventUri lode:inSpace ?spaceUri .
  ?spaceUri rdf:type sf:Point .
  ?spaceUri geosparql:asWKT ?spacePoint .
  ?eventUri smear:hasClassification ?classificationUri .
  ?classificationUri rdfs:label ?classificationLabel .

  FILTER (year(?beginningDateTime) = YEAR
    && month(?beginningDateTime) = MONTH
    && day(?beginningDateTime) = DAY)
}'''

    events_filter_place_query = '''PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX lode: <http://linkedevents.org/ontology/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX sf: <http://www.opengis.net/ont/sf#>
PREFIX geosparql: <http://www.opengis.net/ont/geosparql#>
PREFIX smear: <http://avaa.tdata.fi/web/smart/smear/>

SELECT ?eventUri ?timeUri ?beginningUri ?beginningDateTime
  ?endUri ?endDateTime ?placeUri ?placeName ?placeCountryCode ?placeLocationMap
  ?spaceUri ?spacePoint ?classificationUri ?classificationLabel
WHERE
{
  ?eventUri rdf:type lode:Event .
  ?eventUri lode:atTime ?timeUri .
  ?timeUri rdf:type time:Interval .
  ?timeUri time:hasBeginning ?beginningUri .
  ?beginningUri rdf:type time:Instant .
  ?beginningUri time:inXSDDateTime ?beginningDateTime .
  ?timeUri time:hasEnd ?endUri .
  ?endUri rdf:type time:Instant .
  ?endUri time:inXSDDateTime ?endDateTime .
  ?eventUri lode:atPlace ?placeUri .
  ?placeUri rdf:type dul:Place .
  ?placeUri gn:name ?placeName .
  ?placeUri gn:countryCode ?placeCountryCode .
  ?placeUri gn:locationMap ?placeLocationMap .
  ?eventUri lode:inSpace ?spaceUri .
  ?spaceUri rdf:type sf:Point .
  ?spaceUri geosparql:asWKT ?spacePoint .
  ?eventUri smear:hasClassification ?classificationUri .
  ?classificationUri rdfs:label ?classificationLabel .

  FILTER (?placeName = "PLACE_NAME"^^xsd:string)
}'''

    events_filter_none_query = '''PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX lode: <http://linkedevents.org/ontology/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX dul: <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#>
PREFIX sf: <http://www.opengis.net/ont/sf#>
PREFIX geosparql: <http://www.opengis.net/ont/geosparql#>
PREFIX smear: <http://avaa.tdata.fi/web/smart/smear/>

SELECT ?eventUri ?timeUri ?beginningUri ?beginningDateTime
  ?endUri ?endDateTime ?placeUri ?placeName ?placeCountryCode ?placeLocationMap
  ?spaceUri ?spacePoint ?classificationUri ?classificationLabel
WHERE
{
  ?eventUri rdf:type lode:Event .
  ?eventUri lode:atTime ?timeUri .
  ?timeUri rdf:type time:Interval .
  ?timeUri time:hasBeginning ?beginningUri .
  ?beginningUri rdf:type time:Instant .
  ?beginningUri time:inXSDDateTime ?beginningDateTime .
  ?timeUri time:hasEnd ?endUri .
  ?endUri rdf:type time:Instant .
  ?endUri time:inXSDDateTime ?endDateTime .
  ?eventUri lode:atPlace ?placeUri .
  ?placeUri rdf:type dul:Place .
  ?placeUri gn:name ?placeName .
  ?placeUri gn:countryCode ?placeCountryCode .
  ?placeUri gn:locationMap ?placeLocationMap .
  ?eventUri lode:inSpace ?spaceUri .
  ?spaceUri rdf:type sf:Point .
  ?spaceUri geosparql:asWKT ?spacePoint .
  ?eventUri smear:hasClassification ?classificationUri .
  ?classificationUri rdfs:label ?classificationLabel .
}'''

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
        response = self.query(self.places_query)

        for binding in response['results']['bindings']:
            identifier = binding['placeUri']['value']
            name = binding['placeName']['value']
            country_code = binding['placeCountryCode']['value']
            location_map = binding['placeLocationMap']['value']
            latitude = binding['placeLatitude']['value']
            longitude = binding['placeLongitude']['value']
            Store.places[name] = Place(identifier, name, country_code, location_map, latitude, longitude)

    def load_classifications(self):
        response = self.query(self.classifications_query)

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
            return self.eval_events(self.query(self.events_filter_date_place_query
                                               .replace('PLACE_NAME', place.name)
                                               .replace('YEAR', str(date.year))
                                               .replace('MONTH', str(date.month))
                                               .replace('DAY', str(date.day))))

        if date is not None:
            date = datetime.strptime(date, '%Y-%m-%d')
            return self.eval_events(self.query(self.events_filter_date_query.replace('YEAR', str(date.year))
                                               .replace('MONTH', str(date.month))
                                               .replace('DAY', str(date.day))))

        if place is not None:
            return self.eval_events(self.query(self.events_filter_place_query
                                               .replace('PLACE_NAME', place.name)))

        return self.eval_events(self.query(self.events_filter_none_query))

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
