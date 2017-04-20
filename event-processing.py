from kb.store import Store
from entity.hyytiaelae import Hyytiaelae
from entity.puijo import Puijo
from processing.visualization import mapevents
from processing.statistics import duration

s = Store()
events = s.get_events()

# mapevents(events)

print(duration(events, fun='avg', place=Puijo()))

