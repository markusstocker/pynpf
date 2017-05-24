from store.store import Store
from entity.event import Event


store = Store()


def record(event):
    store.add_event(event)


def event(date, place, beginning, end, classification):
    e = Event(date, places(place))
    e.set_time(beginning, end)
    e.set_classification(classes(classification))
    return e


def places(name):
    return Store.get_place(name)


def classes(label):
    return Store.get_classification(label)


def events(date=None, place=None):
    return store.get_events(date, places(place))




