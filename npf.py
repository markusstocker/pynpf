from smeardata import fetchdata
from smeardataplot import plotdata
# from dirooz.store import Store
# from dirooz.query import Query
# from dirooz.dataset import DataSet

plotdata(fetchdata('2011-03-26'))

# s = Store('http://localhost:3030/npfe-ld/query')
# q = Query('get_dataset_template.rq',
#          {'TIME_FROM': time_from,
#           'TIME_TO': time_to})
# ds = s.get_data_set(q)
# plot_data_set(ds)
