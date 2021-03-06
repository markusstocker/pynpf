from pynpf.smear.dataplotter import plotdata
from pynpf.smear.datafetcher import fetchdata
from pynpf.processing.visualization import imap
from pynpf.processing.statistics import duration
from pynpf.processing.description import describe
from pynpf.factory import event, events, record
from pynpf.smear.utils import datenum2date, date2datenum
#import time

# https://github.com/RDFLib/rdflib/blob/master/rdflib/tools/rdf2dot.py

#print(datenum2date(736487))
#print(date2datenum('2013-04-04'))

# Example 1
#date = '2013-04-04'
#place = 'Hyytiälä'
#beginning = '11:00'
#end = '19:00'
#classification = 'Class Ia'

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
#d = duration(events(), fun='avg', prov={'agent': 'https://orcid.org/0000-0001-5492-3212'})
#print(d.value())
#record(d)

#end = time.time()
#print(end - start)

#describe(events(place=place), format='graph')


