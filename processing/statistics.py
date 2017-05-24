import dateutil.parser
import datetime


def duration(events, fun='avg'):
    timedeltas = list()

    for event in events:
        at_time = event.get_at_time()
        beginning = at_time.get_beginning().get_datetime()
        end = at_time.get_end().get_datetime()
        timedeltas.append((end-beginning))

    if fun == 'avg':
        print(sum(timedeltas, datetime.timedelta(0)) / len(timedeltas))
    elif fun == 'max':
        print(max(timedeltas))
    elif fun == 'min':
        print(min(timedeltas))
    else:
        raise ValueError('Unsupported function: {}'.format(fun))

