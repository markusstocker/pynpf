from smear.datafetcher import fetchdata
from smear.dataplotter import plotdata
from smear.datawriter import writedata
from smear.datareader import readdata
from datetime import date, timedelta
from time import sleep


start_day = date(2015, 1, 1)
end_day = date(2015, 12, 31)
current_day = start_day

place = 'Hyytiälä' # Hyytiälä, Puijo, Värriö
placename = 'hyytiaelae' # hyytiaelae, puijo, vaerrioe

while current_day <= end_day:
    filename = '{}_{}.csv'.format(placename, current_day.strftime('%Y-%m-%d'))
    file = '/home/ms/workspace-pynpf/pynpf-data/observational/{}/{}'.format(placename, filename)

    writedata(fetchdata(current_day.strftime('%Y-%m-%d'), place), file)
    current_day = current_day + timedelta(days=1)

    sleep(1)
    #plotdata(readdata(file))


