from rdflib import Namespace


ns = Namespace('http://purl.obolibrary.org/obo/')

# formation of particles in an atmosphere is an atmospheric process and a particle formation process
# that has some aerosol as output and occurs in some atmosphere

ENVO_01001085 = ns['ENVO_01001085']  # formation of particles in an atmosphere
ENVO_02500003 = ns['ENVO_02500003']  # atmospheric process
ENVO_01001084 = ns['ENVO_01001084']  # particle formation process
ENVO_02500000 = ns['ENVO_02500000']  # environmental system process
ENVO_00010505 = ns['ENVO_00010505']  # aerosol
ENVO_01000060 = ns['ENVO_01000060']  # particulate matter
ENVO_01000267 = ns['ENVO_01000267']  # atmosphere
