from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from entity.event import Event
from entity.puijo import Puijo
from entity.hyytiaelae import Hyytiaelae
from entity.vaerrioe import Vaerrioe
from kb.store import Store
from processing.visualization import mapevents
from processing.statistics import duration
from processing.description import describe
from datetime import datetime, timedelta


date = '2013-04-04'
place = Hyytiaelae()

plotdata(fetchdata(date, place))

# e = Event(date=date, place=Hyytiaelae())
# e.at_time(beginning='12:00', end='17:00')

#s = Store()
# s.add_event(e)

# events = s.get_events()
# mapevents(events)
# print(duration(events, fun='avg', place=Hyytiaelae()))

#event = s.get_event(date=date, place=Hyytiaelae())
#describe(event, format='text')

#matlab_datenum = 735328
#python_datetime = datetime.fromordinal(int(matlab_datenum)) + timedelta(days=matlab_datenum%1) - timedelta(days = 366)
#print(python_datetime)
