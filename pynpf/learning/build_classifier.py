import pandas as pd
import os.path
from datetime import date, timedelta
from pynpf.learning.featurizer import feature_vector
from pynpf.smear import date2datenum
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib

location = 'hyytiaelae'
start_day = date(2007, 1, 1)
end_day = date(2014, 12, 31)
current_day = start_day
cls_period = '1996-2016'
dir = '/home/ms/workspace-pynpf/pynpf-data'

X = []
Y = []
#labels = ['Class Ia', 'Class Ib', 'Class II', 'Non Event']
#label_count = {'Class Ia': 0, 'Class Ib': 0, 'Class II': 0, 'Non Event': 0}
labels = ['Event', 'Non Event']
label_count = {'Event': 0, 'Non Event': 0}


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

#        if label == 'Non Event' and label_count['Non Event'] > 682:
#            print('Skip {} (excessive non events)'.format(current_day_str))
#            current_day = current_day + timedelta(days=1)
#            continue

        label_count[label] = label_count[label] + 1

        vector = feature_vector(obs_data)

        X.append(vector)
        Y.append(label)

        current_day = current_day + timedelta(days=1)

    print('Number of samples {} and labels {}'.format(len(X), len(Y)))
    print(label_count)

    if len(X) == 0:
        exit(0)

    scaler = MinMaxScaler()
    scaler.fit(X)

    joblib.dump(scaler, 'models/scaler-event-detection.pkl')

    X = scaler.transform(X)

    classifier = MLPClassifier(solver='lbfgs', hidden_layer_sizes=[2], max_iter=2000, activation='logistic')
#    classifier = SVC()

    classifier.fit(X, Y)

    joblib.dump(classifier, 'models/classifier-event-detection.pkl')
