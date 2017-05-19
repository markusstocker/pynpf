from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from entity.event import Event
from entity.puijo import Puijo
from entity.hyytiaelae import Hyytiaelae
from entity.vaerrioe import Vaerrioe
from entity.classIa import ClassIa
from entity.classIb import ClassIb
from entity.classII import ClassII
from kb.store import Store
from processing.visualization import map
from processing.statistics import duration
from processing.description import describe
from datetime import datetime, timedelta
from smear.utils import date2datenum
from factory import record, event, events
from smear.utils import date2datenum, datenum2date
import time


#print(datenum2date(735117))

# Example 1
date = '2013-04-04' # Event Class Ia
#date = '2012-09-07' # Non event
place = Hyytiaelae()
beginning = '11:00'
end = '19:00'
classification = ClassIa()

# Example 2
#date = '2015-03-10'
#place = Vaerrioe()
#beginning = '09:00'
#end = '15:00'
#classification = ClassIb()

# Examoke 3
#date = '2011-06-05'
#place = Puijo()

#plotdata(fetchdata(date, place))

#record(event(date, place, beginning='09:00', end='15:00', classification=ClassIb()))

#map(events())

#start = time.time()
#duration(events(), fun='avg')
#end = time.time()
#print(end - start)

#describe(events(query='construct'), format='rdf')

