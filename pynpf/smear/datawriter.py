import pandas as pd


def writedata(data, file, type='csv'):
    if type == 'csv':
        data.to_csv(file, index=False, encoding='utf-8')
    elif type == 'rdf':
        to_rdf(data, file)
    else:
        raise ValueError('Unsupported type: {}'.format(type))


def to_rdf(data, file):
    raise ValueError('Unsupported type: rdf')