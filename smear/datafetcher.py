import requests
import csv
import io
from urllib.parse import urlencode
from datetime import datetime, timedelta
from pytz import timezone


configuration = {
    'Hyytiälä': {
        'smear_table': 'HYY_DMPS',
        'smear_variables': 'd316e1,d355e1,d398e1,d447e1,d501e1,d562e1,d631e1,d708e1,d794e1,'\
                           'd891e1,d100e2,d112e2,d126e2,d141e2,d158e2,d178e2,d200e2,d224e2,'\
                           'd251e2,d282e2,d316e2,d355e2,d398e2,d447e2,d501e2,d562e2,d631e2,'\
                           'd708e2,d794e2,d891e2,d100e3,d112e3,d126e3,d141e3,d158e3,d178e3,d200e3'
    },
    'Puijo': {
        'smear_table': 'PUI_dmps_tot',
        'smear_variables': 'ch01,ch02,ch03,ch04,ch05,ch06,ch07,ch08,ch09,ch10,ch11,ch12,ch13,ch14,ch15,ch16,'\
                           'ch17,ch18,ch19,ch20,ch21,ch22,ch23,ch24,ch25,ch26,ch27,ch28,ch29,ch30,ch31,ch32,'\
                           'ch33,ch34,ch35,ch36,ch37,ch38,ch39,ch40'
    },
    'Värriö': {
        'smear_table': 'VAR_DMPS',
        'smear_variables': 'd316e1,d355e1,d398e1,d447e1,d501e1,d562e1,d631e1,d708e1,d794e1,'\
                           'd891e1,d100e2,d112e2,d126e2,d141e2,d158e2,d178e2,d200e2,d224e2,'\
                           'd251e2,d282e2,d316e2,d355e2,d398e2,d447e2,d501e2,d562e2,d631e2,'\
                           'd708e2,d794e2,d891e2,d100e3,d112e3,d126e3,d141e3,d158e3,d178e3,d200e3'
    }
}


def fetchdata(date, place):
    time_from = timezone('Europe/Helsinki').localize(datetime.strptime(date, '%Y-%m-%d'))
    time_to = time_from + timedelta(days=1)

    try:
        smear_table = configuration[place]['smear_table']
        smear_variables = configuration[place]['smear_variables']
    except LookupError:
        print('Place not found in configuration [place = {}, places = {}]'.format(place, configuration.keys()))
        return list()

    query = {'table': smear_table, 'quality': 'ANY', 'averaging': 'NONE', 'type': 'NONE',
             'from': str(time_from), 'to': str(time_to), 'variables': smear_variables}
    url = 'http://avaa.tdata.fi/smear-services/smeardata.jsp?' + urlencode(query)
    response = requests.post(url)

    return list(csv.reader(io.StringIO(response.text)))
