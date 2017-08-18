import pandas as pd
import numpy as np
from store.store import Store
from entity.event import Event
from learning.featurizer import feature_vector
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib


store = Store()
mlp_detection = joblib.load('learning/models/event-detection.pkl')


def assess(data):
    vector = feature_vector(data)
    pre_detection = mlp_detection.predict(np.array(vector).reshape(1, -1))
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
