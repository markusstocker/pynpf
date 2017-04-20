from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from entity.event import Event
from entity.puijo import Puijo
from entity.hyytiaelae import Hyytiaelae
from kb.store import Store
from processing.visualization import mapevents
from processing.statistics import duration


# date = '2011-03-26'

# plotdata(fetchdata(date))

# e = Event(date=date, place=Puijo())
# e.at_time(beginning='11:00', end='17:00')

s = Store()
# s.add_event(e)

events = s.get_events()

# mapevents(events)

print(duration(events, fun='avg'))

