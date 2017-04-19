from rdflib import Namespace


ns = Namespace('http://www.w3.org/2006/time#')

Instant = ns['Instant']
Interval = ns['Interval']
hasBeginning = ns['hasBeginning']
hasEnd = ns['hasEnd']
inXSDDateTime = ns['inXSDDateTime']