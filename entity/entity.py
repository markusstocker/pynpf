from rdflib import URIRef


class Entity:
    def __init__(self, identifier=None):
        self.identifier = None
        self.uri = None
        self.set_identifier(identifier)

    def set_identifier(self, identifier):
        if self.identifier is None:
            self.identifier = identifier
            self.uri = URIRef(self.identifier)
            return

        if self.identifier != identifier:
            raise ValueError('Incompatible identifiers {} {}'.format(self.identifier, identifier))

    def get_identifier(self):
        return self.identifier

