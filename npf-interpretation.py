from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from entity.event import Event
from kb.store import Store

date = '2011-03-26'

plotdata(fetchdata(date))

e = Event(date)
e.at_time(beginning='12:00', end='17:00')

s = Store()
s.add_event(e)

# q = Query('get_dataset_template.rq',
#          {'TIME_FROM': time_from,
#           'TIME_TO': time_to})
