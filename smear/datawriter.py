import csv


def writedata(data, file):
    with open(file, 'w') as f:
        w = csv.writer(f)
        w.writerows(data)
