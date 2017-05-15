from kb.store import Store
from entity.event import Event


def record(event):
    Store().add_event(event)


def event(date, place, beginning, end, eventclass):
    e = Event(date=date, place=place)
    e.at_time(beginning=beginning, end=end)
    e.event_class(eventclass)
    return e


def getevent(date, place):
    return Store().get_event(date, place)


def getevents():
    return Store().get_events()



