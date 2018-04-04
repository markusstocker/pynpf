from hashlib import md5
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from pynpf.entity.entity import Entity
from pynpf.vocab import Base, OBI, IAO, BFO, PROV


class AverageValue(Entity):
    def __init__(self, value_specification=None, dataset=None, prov=None):
        self.value_specification = value_specification
        self.dataset = dataset  # This is a list of events
        self.dataset_uri = None
        self.prov = prov

        if self.dataset is not None:
            hash = 1234567890
            for element in self.dataset:
                hash = hash + element.__hash__()
            self.dataset_uri = '{}{}'.format(Base.ns,
                                             md5('{}'.format(hash).encode()).hexdigest())

        if self.value_specification is not None and self.dataset is not None:
            hash = self.value_specification.__hash__() + self.dataset_uri.__hash__()

            super().__init__('{}{}'.format(Base.ns,
                                           md5('{}'.format(hash).encode()).hexdigest()))

    def value(self):
        return self.value_specification.value()

    def graph(self):
        dataset = URIRef(self.dataset_uri)
        g = Graph()
        g.add((self.uri, RDF.type, OBI.OBI_0000679))
        g.add((self.uri, OBI.OBI_0001938, self.value_specification.uri))
        g.add((self.uri, IAO.IAO_0000136, dataset))

        for s, p, o in self.value_specification.graph():
            g.add((s, p, o))

        g.add((dataset, RDF.type, IAO.IAO_0000100))

        for element in self.dataset:
            g.add((dataset, BFO.BFO_0000051, element.uri))

        g.add((self.uri, RDF.type, PROV.Entity))
        g.add((dataset, RDF.type, PROV.Entity))
        g.add((self.uri, PROV.wasDerivedFrom, dataset))

        if self.prov is None:
            return g

        agent = None
        activity = None

        if 'agent' in self.prov:
            agent = URIRef(self.prov['agent'])
            g.add((agent, RDF.type, PROV.Agent))
            g.add((self.uri, PROV.wasAttributedTo, agent))

        if 'activity' in self.prov:
            activity = URIRef(self.prov['activity'])
            g.add((activity, RDF.type, PROV.Activity))
            g.add((self.uri, PROV.wasGeneratedBy, activity))
            g.add((activity, PROV.used, dataset))

        if agent is not None and activity is not None:
            g.add((activity, PROV.wasAssociatedWith, agent))

        return g