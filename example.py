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
from processing.visualization import mapevents
from processing.statistics import duration
from processing.description import describe
from datetime import datetime, timedelta
from smear.utils import date2datenum
from factory import record, event, getevent, getevents
from smear.utils import date2datenum, datenum2date


#print(datenum2date(736033))

# Example 1
#date = '2013-04-04'
#place = Hyytiaelae()
#beginning = '11:00'
#end = '20:00'
#eventclass = ClassIa()

# Example 2
#date = '2015-03-10'
#place = Vaerrioe()
#beginning = '09:00'
#end = '15:00'
#eventclass = ClassIb()

# Examoke 3
date = '2011-06-05'
place = Hyytiaelae()

plotdata(fetchdata(date, place))

#record(event(date, place, beginning, end, eventclass))

mapevents(getevents())
#print(duration(getevents(), fun='avg', place=place))

#describe(getevent(date, place), format='text')

