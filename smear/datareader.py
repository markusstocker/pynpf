import csv


def readdata(file):
    with open(file, 'r') as f:
        r = csv.reader(f)
        return list(r)
