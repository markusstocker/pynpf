import requests
import csv
import io
from entity.hyytiaelae import Hyytiaelae
from urllib.parse import urlencode
from datetime import datetime, timedelta
from pytz import timezone


def fetchdata(date, place=Hyytiaelae()):
    tz = timezone('Europe/Helsinki')
    time_from = tz.localize(datetime.strptime(date, '%Y-%m-%d'))
    time_to = time_from + timedelta(days=1)
    smear_table = place.smear_table
    smear_variables = place.smear_variables

    query = {'table': smear_table, 'quality': 'ANY', 'averaging': 'NONE', 'type': 'NONE',
             'from': str(time_from), 'to': str(time_to), 'variables': smear_variables}
    url = 'http://avaa.tdata.fi/smear-services/smeardata.jsp?' + urlencode(query)
    response = requests.post(url)

    return list(csv.reader(io.StringIO(response.text)))
