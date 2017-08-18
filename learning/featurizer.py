import numpy as np
from datetime import datetime
from sklearn.decomposition import TruncatedSVD


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
        np.sum(data_nighttime_new),
        np.max(data_nighttime_new),
        np.min(data_nighttime_new),
        np.var(data_nighttime_new),
        np.sum(data_daytime_new) - np.sum(data_nighttime_new),
        np.max(data_daytime_new) - np.max(data_nighttime_new),
        np.min(data_daytime_new) - np.min(data_nighttime_new),
        np.var(data_daytime_new) - np.var(data_nighttime_new)
    ]
    return ret

