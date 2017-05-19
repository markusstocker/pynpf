import dateutil.parser
import datetime


def duration(events, fun='avg'):
    timedeltas = list()

    for event in events['results']['bindings']:
        beginning = dateutil.parser.parse(event['beginningDateTime']['value'])
        end = dateutil.parser.parse(event['endDateTime']['value'])
        timedeltas.append((end-beginning))

    if fun == 'avg':
        print(sum(timedeltas, datetime.timedelta(0)) / len(timedeltas))
    elif fun == 'max':
        print(max(timedeltas))
    elif fun == 'min':
        print(min(timedeltas))
    else:
        raise ValueError('Unsupported function: {}'.format(fun))

