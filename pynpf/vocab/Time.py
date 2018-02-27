from rdflib import Namespace


ns = Namespace('http://www.w3.org/2006/time#')

Instant = ns['Instant']
Interval = ns['Interval']
Duration = ns['Duration']
TemporalUnit = ns['TemporalUnit']
hasTime = ns['hasTime']
hasBeginning = ns['hasBeginning']
hasEnd = ns['hasEnd']
numericDuration = ns['numericDuration']
unitType = ns['unitType']
inXSDDateTime = ns['inXSDDateTime']
unitHour = ns['unitHour']