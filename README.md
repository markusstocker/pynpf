## Requirements

sudo apt-get install python3-mpltoolkits.basemap
sudo pip3 install rdflib
sudo pip3 install geomet
sudo pip3 install rdflib-jsonld
sudo pip3 install pandas
sudo pip3 install scipy
sudo pip3 install scikit-learn

ipyleaflet
sudo pip install ipyleaflet
sudo jupyter nbextension enable --py --sys-prefix ipyleaflet
sudo jupyter nbextension enable --py --sys-prefix widgetsnbextension
See also: http://jupyter.org/widgets.html
See also: https://github.com/ellisonbg/ipyleaflet/

JupyterHub
sudo apt-get install npm nodejs-legacy
sudo python3 -m pip install jupyterhub
sudo npm install -g configurable-http-proxy
See also: http://jupyterhub.readthedocs.io/en/latest/quickstart.html

sudo apt-get install texlive-xetex

## Tests

python -m unittest discover

https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure