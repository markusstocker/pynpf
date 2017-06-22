## Requirements

sudo apt-get install python3-mpltoolkits.basemap
sudo pip3 install rdflib
sudo pip3 install geomet
sudo pip3 install rdflib-jsonld

ipyleaflet
sudo pip install ipyleaflet
sudo jupyter nbextension enable --py --sys-prefix ipyleaflet
sudo jupyter nbextension enable --py --sys-prefix widgetsnbextension
See also: http://jupyter.org/widgets.html
See also: https://github.com/ellisonbg/ipyleaflet/

## Tests

python -m unittest discover

https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure