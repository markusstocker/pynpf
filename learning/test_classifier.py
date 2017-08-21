import pandas as pd
import os.path
from datetime import date, timedelta
from learning.featurizer import feature_vector
from smear.utils import date2datenum
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib

location = 'hyytiaelae'
cls_period = '1996-2016'
start_day = date(2015, 1, 1)
end_day = date(2015, 12, 31)
current_day = start_day
labels = ['Event', 'Non Event']
dir = '/home/ms/workspace-pynpf/pynpf-data'

X = []
Y = []

mlp = joblib.load('models/event-detection.pkl')

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

        if len(cls_data_day) == 0:
            print('Skip {} (no classification)'.format(current_day_str))
            current_day = current_day + timedelta(days=1)
            continue

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

        X.append(vector)
        Y.append(label)

        current_day = current_day + timedelta(days=1)

    print('Number of samples: {}'.format(len(X)))

    if len(X) == 0:
        exit(0)

    scaler = MinMaxScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100)

    Y_pred = mlp.predict(X_test)

    print(accuracy_score(Y_test, Y_pred) * 100)
    print(confusion_matrix(Y_test, Y_pred, labels=labels))
    print(classification_report(Y_test, Y_pred, target_names=labels))
