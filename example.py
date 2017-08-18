from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from smear.datareader import readdata
from smear.datawriter import writedata
from entity.event import Event
from store.store import Store
from processing.visualization import smap
from processing.statistics import duration
from processing.description import describe
from datetime import datetime, timedelta
from smear.utils import date2datenum
from entity.point import Point
from factory import assess, record, event, events, places, classes
from smear.utils import date2datenum, datenum2date
import time


#print(datenum2date(736711))
print(date2datenum('2016-01-01'))

# Example 1
date = '2013-04-04'
place = 'Hyytiälä'
beginning = '11:00'
end = '19:00'
classification = 'Class Ia'

# Example 2
#date = '2015-03-10'
#place = 'Värriö'
#beginning = '09:00'
#end = '15:00'
#classification = 'Class Ib'

# Example 3
#date = '2011-06-05'
#place = 'Puijo'
#beginning = '10:00'
#end = '17:00'
#classification = 'Class Ia'

#plotdata(fetchdata(date, place))

#writedata(fetchdata(date, place), '/tmp/test.csv')
#plotdata(readdata('/tmp/test.csv'))

#assess(fetchdata(date, place))

#record(event(date, place, beginning, end, classification))

#smap(events())

#start = time.time()
#duration(events(), fun='avg')
#end = time.time()
#print(end - start)

#describe(events(place=place), format='rdf')


