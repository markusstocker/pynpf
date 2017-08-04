import csv
import pandas as pd
import numpy as np
from datetime import date, timedelta
from learning.featurizer import featurize
from smear.datareader import readdata
from smear.dataplotter import plotdata
from smear.utils import date2datenum, datenum2date
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.decomposition import TruncatedSVD

location = 'hyytiaelae'
start_day = date(2013, 1, 1)
end_day = date(2013, 12, 31)
current_day = start_day
example_day = date(2013, 4, 4)
cls_period = '1996-2016'
dir = '/home/ms/workspace-pynpf/pynpf-data'

X = []
Y = []
X_example = []
labels = ['Class Ia', 'Class Ib', 'Class II']
labels = ['Event', 'Non Event']

# Create labelled dataset
while current_day <= end_day:
    current_day_str = current_day.strftime('%Y-%m-%d')

    cls_data_file = '{}/classification/{}_dmps_event_classification_{}.txt'.format(dir, location, cls_period)
    cls_data = pd.read_csv(cls_data_file, sep=' ', header=None, names=['Matlab Datenum', 'Class Ia', 'Class Ib',
                                                                       'Class II', 'N/A', 'N/A', 'N/A', 'N/A',
                                                                       'Non Event', 'Undefined', 'Bad Data',
                                                                       'Partly Bad Data', 'Checksum'])

    date_num = int(date2datenum(current_day_str))
    cls_data_day = cls_data.loc[cls_data['Matlab Datenum'] == date_num]

    if cls_data_day.iloc[0]['Class Ia'] == 1:
        label = 'Event'
    elif cls_data_day.iloc[0]['Class Ib'] == 1:
        label = 'Event'
    elif cls_data_day.iloc[0]['Class II'] == 1:
        label = 'Event'
    elif cls_data_day.iloc[0]['Non Event'] == 1:
        label = 'Non Event'
    else:
        print('Skip {} (class)'.format(current_day_str))
        current_day = current_day + timedelta(days=1)
        continue

    obs_data_file = '{}/observational/{}/{}_{}.csv'.format(dir, location, location, current_day_str)
    obs_data = pd.read_csv(obs_data_file)

    # obs_data = obs_data.loc[(obs_data['Hour'] >= 6) & (obs_data['Hour'] <= 18)]

    if obs_data.isnull().values.any():
        print('Skip {} (is null)'.format(current_day_str))
        current_day = current_day + timedelta(days=1)
        continue

    svd = TruncatedSVD(n_components=1)
    svd_data = svd.fit_transform(obs_data.ix[:, 6:].transpose())
    svd_data = [item for sublist in svd_data for item in sublist]

    if current_day == example_day:
        X_example = svd_data

    X.append(svd_data)
    Y.append(label)

    current_day = current_day + timedelta(days=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

mlp = MLPClassifier()
mlp.fit(X_train, Y_train)

Y_pred = mlp.predict(X_test)

print(accuracy_score(Y_test, Y_pred)*100)
print(confusion_matrix(Y_test, Y_pred, labels=labels))
print(classification_report(Y_test, Y_pred, target_names=labels))

print(mlp.predict([X_example]))
