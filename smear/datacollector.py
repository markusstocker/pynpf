from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from smear.datawriter import writedata
from smear.datareader import readdata

date = '2013-12-31'

place = 'Värriö' # Hyytiälä, Puijo, Värriö
placename = 'vaerrioe' # hyytiaelae, puijo, vaerrioe

filename = '{}_{}.csv'.format(placename, date)
file = '/home/ms/workspace-pynpf/pynpf-data/observational/{}/{}'.format(placename, filename)

#writedata(fetchdata(date, place), file)
#plotdata(readdata(file))


