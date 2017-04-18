from smeardata import fetchdata
from smeardataplot import plotdata
from dirooz.store import Store
from dirooz.query import Query
from dirooz.dataset import DataSet

date = '2011-03-26'
data_set = fetchdata(date)
plotdata(data_set)

# s = Store('http://localhost:3030/npfe-ld/query')
# q = Query('get_dataset_template.rq',
#          {'TIME_FROM': time_from,
#           'TIME_TO': time_to})
# ds = s.get_data_set(q)
# plot_data_set(ds)
