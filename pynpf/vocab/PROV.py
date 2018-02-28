from rdflib import Namespace


ns = Namespace('http://www.w3.org/ns/prov#')

Entity = ns['Entity']
Activity = ns['Activity']
Agent = ns['Agent']
wasDerivedFrom = ns['wasDerivedFrom']
wasGeneratedBy = ns['wasGeneratedBy']
wasAttributedTo = ns['wasAttributedTo']
wasAssociatedWith = ns['wasAssociatedWith']
used = ns['used']
