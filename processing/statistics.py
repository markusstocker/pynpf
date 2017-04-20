import dateutil.parser
import datetime


def duration(events, fun='avg', place=None):
    timedeltas = list()

    for binding in events['results']['bindings']:
        if place is not None:
            print(place.name + ' ' + binding['placeName']['value'])
            print(place.name != binding['placeName']['value'])
            if place.name != binding['placeName']['value']:
                continue
        beginning = dateutil.parser.parse(binding['beginningDateTime']['value'])
        end = dateutil.parser.parse(binding['endDateTime']['value'])
        timedeltas.append((end-beginning))

    if fun == 'avg':
        return sum(timedeltas, datetime.timedelta(0)) / len(timedeltas)
    if fun == 'max':
        return max(timedeltas)
    if fun == 'min':
        return min(timedeltas)

    raise ValueError('Unsupported function: {}'.format(fun))
