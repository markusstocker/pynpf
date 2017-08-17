import csv
import pandas as pd
import numpy as np
import os.path
from datetime import date, timedelta
from learning.featurizer import featurize
from smear.datareader import readdata
from smear.dataplotter import plotdata
from smear.utils import date2datenum, datenum2date
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import MinMaxScaler

location = 'hyytiaelae'
start_day = date(2010, 1, 1)
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


def svd_vector(data):
    svd = TruncatedSVD(n_components=1)
    vector = svd.fit_transform(data.ix[:, 6:].transpose())
    return [item for sublist in vector for item in sublist]


def feature_vector(data):
#    data_day = data.ix[:, 6:].as_matrix()
#    data_daytime = data.loc[(data['Hour'] >= 9) & (data['Hour'] <= 15)].ix[:, 6:].as_matrix()
    data_day_new = data.ix[:, 6:16].as_matrix()  # Number concentration of particles with diameter <= 7nm (13) 15nm (20)
    data_daytime_new = data.loc[(data['Hour'] >= 9) & (data['Hour'] <= 15)].ix[:, 6:20].as_matrix()
    data_nighttime_new = data.loc[(data['Hour'] < 9) | (data['Hour'] > 15)].ix[:, 6:20].as_matrix()
    ret = [
        np.sum(data_day_new),
        np.max(data_day_new),
        np.min(data_day_new),
        np.var(data_day_new),
#        np.sum(data_nighttime_new),
#        np.max(data_nighttime_new),
#        np.min(data_nighttime_new),
#        np.var(data_nighttime_new),
#        np.sum(data_daytime_new) - np.sum(data_nighttime_new),
#        np.max(data_daytime_new) - np.max(data_nighttime_new),
#        np.min(data_daytime_new) - np.min(data_nighttime_new),
#        np.var(data_daytime_new) - np.var(data_nighttime_new)
    ]
    return ret

if __name__ == "__main__":
    cls_data_file = '{}/classification/{}_dmps_event_classification_{}.txt'.format(dir, location, cls_period)
    cls_data = pd.read_csv(cls_data_file, sep=' ', header=None, names=['Matlab Datenum', 'Class Ia', 'Class Ib',
                                                                       'Class II', 'N/A', 'N/A', 'N/A', 'N/A',
                                                                       'Non Event', 'Undefined', 'Bad Data',
                                                                       'Partly Bad Data', 'Checksum'])

    # Create labelled dataset
    while current_day <= end_day:
        current_day_str = current_day.strftime('%Y-%m-%d')

        print('Processing day {}'.format(current_day_str))

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
            print('Skip {} (unsupported class)'.format(current_day_str))
            current_day = current_day + timedelta(days=1)
            continue

        obs_data_file = '{}/observational/{}/{}_{}.csv'.format(dir, location, location, current_day_str)

        if not os.path.isfile(obs_data_file):
            print('Skip {} (file not found)'.format(current_day_str))
            current_day = current_day + timedelta(days=1)
            continue

        obs_data = pd.read_csv(obs_data_file)

        if obs_data.isnull().values.any():
            print('Skip {} (is null)'.format(current_day_str))
            current_day = current_day + timedelta(days=1)
            continue

        if len(obs_data) == 0:
            print('Skip {} (no data)'.format(current_day_str))
            current_day = current_day + timedelta(days=1)
            continue

        vector = feature_vector(obs_data)

        if current_day == example_day:
            X_example = vector

        X.append(vector)
        Y.append(label)

        current_day = current_day + timedelta(days=1)

    print('Number of samples: {}'.format(len(X)))

    scaler = MinMaxScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

    mlp = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[2], max_iter=2000, activation='logistic')
    mlp.fit(X_train, Y_train)

    Y_pred = mlp.predict(X_test)

    print(accuracy_score(Y_test, Y_pred) * 100)
    print(confusion_matrix(Y_test, Y_pred, labels=labels))
    print(classification_report(Y_test, Y_pred, target_names=labels))

    print(mlp.predict([X_example]))


