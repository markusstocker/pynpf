import numpy as np
from pynpf.store.store import Store
from pynpf.entity.event import Event
from pynpf.learning.featurizer import feature_vector
from sklearn.externals import joblib


store = Store()
classifier_detection = joblib.load('pynpf/learning/models/classifier-event-detection.pkl')
scaler_detection = joblib.load('pynpf/learning/models/scaler-event-detection.pkl')


def assess(data):
    vector = feature_vector(data)
    vector = np.array(vector).reshape(1, -1)
    vector = scaler_detection.transform(vector)
    pre_detection = classifier_detection.predict(vector)
    print(pre_detection)


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