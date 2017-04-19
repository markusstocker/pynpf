import requests
import csv
import io
from urllib.parse import urlencode
from datetime import datetime, timedelta
from pytz import timezone


def fetchdata(date):
    tz = timezone('Europe/Helsinki')
    time_from = tz.localize(datetime.strptime(date, '%Y-%m-%d'))
    time_to = time_from + timedelta(days=1)

    variables = 'd316e1,d355e1,d398e1,d447e1,d501e1,d562e1,d631e1,d708e1,d794e1,' \
                'd891e1,d100e2,d112e2,d126e2,d141e2,d158e2,d178e2,d200e2,d224e2,' \
                'd251e2,d282e2,d316e2,d355e2,d398e2,d447e2,d501e2,d562e2,d631e2,' \
                'd708e2,d794e2,d891e2,d100e3,d112e3,d126e3,d141e3,d158e3,d178e3,d200e3'
    query = {'table': 'HYY_DMPS', 'quality': 'ANY', 'averaging': 'NONE', 'type': 'NONE',
             'from': time_from, 'to': time_to, 'variables': variables}
    url = 'http://avaa.tdata.fi/palvelut/smeardata.jsp?' + urlencode(query)
    response = requests.post(url)

    return list(csv.reader(io.StringIO(response.text)))
