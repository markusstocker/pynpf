from learning.featurizer import featurize
from smear.datareader import readdata
from smear.dataplotter import plotdata

dir = '/home/ms/workspace-pynpf/pynpf-data/observational'
file = '{}/{}/{}'.format(dir, 'hyytiaelae', 'hyytiaelae_2013-04-04.csv')

data = readdata(file)

plotdata(data)

features = featurize(data)

print(features)


