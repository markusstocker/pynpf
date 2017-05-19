from kb.store import Store
from entity.event import Event


def record(event):
    Store().add_event(event)


def event(date, place, beginning, end, classification):
    e = Event(date=date, place=place)
    e.at_time(beginning=beginning, end=end)
    e.event_class(classification)
    return e


def events(date=None, place=None, query='select'):
    return Store().get_events(date, place, query)




