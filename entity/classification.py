from rdflib import Graph
from vocab import SmartSMEAR
from rdflib.namespace import RDF
from rdflib.namespace import RDFS
from entity.entity import Entity


class Classification(Entity):

    def __init__(self, identifier, label, comment):
        super().__init__(identifier)
        self.label = label
        self.comment = comment

    def get_label(self):
        return self.label

    def get_comment(self):
        return self.comment



