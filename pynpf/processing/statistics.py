import datetime
from pynpf.vocab import OBI
from pynpf.entity.duration import Duration
from pynpf.entity.averagevalue import AverageValue


def duration(events, fun='avg', prov={}):
    timedeltas = list()

    for event in events:
        at_time = event.get_at_time()
        beginning = at_time.get_beginning().get_datetime()
        end = at_time.get_end().get_datetime()
        timedeltas.append((end-beginning))

    if fun == 'avg':
        avg_timedelta = sum(timedeltas, datetime.timedelta(0)) / len(timedeltas)
        if 'activity' not in prov:
            prov['activity'] = OBI.OBI_0200170
        return AverageValue(Duration(avg_timedelta), events, prov)
    elif fun == 'max':
        print(max(timedeltas))
    elif fun == 'min':
        print(min(timedeltas))
    else:
        raise ValueError('Unsupported function: {}'.format(fun))

