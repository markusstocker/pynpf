from rdflib import Namespace


ns = Namespace('http://avaa.tdata.fi/web/smart/smear/')

EventClass = ns['EventClass']
hasEventClass = ns['hasEventClass']

# dal Maso et al. (2005): Formation and growth of fresh atmospheric aerosols: eight years of aerosol size
# distribution data from SMEAR II, Hyytiälä, Finland, BOREAL ENVIRONMENT RESEARCH 10: 323–336

# Class I: Days when the growth and formation rate could be determined with a good confidence level

# Class Ia: Very clear and strong particle formation events, with little or no pre-existing particles obscuring the
# newly formed mode, making them suitable for modeling case studies of NPF events
ClassIa = ns['ClassIa']

# Class Ib: Rest of class I events
ClassIb = ns['ClassIb']

# Class II: Days where the derivation of these parameters was not possible or the accuracy of the results was
# questionable
ClassII = ns['ClassII']
