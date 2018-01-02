import pandas as pd


def writedata(data, file):
    data.to_csv(file, index=False, encoding='utf-8')
