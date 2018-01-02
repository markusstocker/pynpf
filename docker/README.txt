sudo docker build -t jupyterhub . 
sudo docker run --name fuseki -p 3030:3030 -e ADMIN_PASSWORD=admin -d stain/jena-fuseki
sudo docker run --name jupyterhub -p 8000:8000 --net="host" -d jupyterhub jupyterhub

sudo docker start fuseki
sudo docker start jupyterhub

sudo docker exec -it jupyterhub bash

sudo docker stop jupyterhub
sudo docker rm jupyterhub
sudo docker rmi jupyterhub
sudo docker rmi jupyterhub/jupyterhub

sudo docker stop fuseki
sudo docker rm fuseki
sudo docker rmi stain/jena-fuseki

==== DEPRECATED ====

docker pull ubuntu
docker run -p 3030:3030 -p 8888:8888 -it ubuntu /bin/bash
apt-get update
apt-get install git
apt-get install python3
apt-get install python3-pip
pip3 install --upgrade pip 
pip3 install jupyter
apt-get install python3-mpltoolkits.basemap
pip3 install requests
pip3 install rdflib
pip3 install geomet
pip3 install rdflib-jsonld
pip3 install pandas
pip3 install scipy
pip3 install scikit-learn
pip install ipyleaflet
jupyter nbextension enable --py --sys-prefix ipyleaflet
jupyter nbextension enable --py --sys-prefix widgetsnbextension
git clone https://github.com/markusstocker/pynpf.git /opt/pynpf
git clone https://markusstocker@bitbucket.org/markusstocker/pynpf-data.git /opt/pynpf-data
/opt/apache-jena-fuseki-2.5.0/run/shiro.ini: /$/** = anon
jupyter notebook --generate-config
jupyter notebook password

docker images
docker ps -a
docker start CONTAINER
docker exec -it CONTAINER bash
jupyter notebook --allow-root --ip 0.0.0.0 --no-browser /opt/pynpf &> /dev/null &
export JAVA_HOME=/opt/jdk1.8.0_74
/opt/apache-jena-fuseki-2.5.0/fuseki-server &> /dev/null &

jupyter notebook list
jupyter notebook stop 8888

docker stop CONTAINER
docker commit CONTAINER IMAGE  
docker save IMAGE > IMAGE.tar  
docker load < IMAGE.tar 

# Build classifer
export PYTHONPATH=${PYTHONPATH}:/opt/pynpf
build_classifier.py: dir = '/opt/pynpf-data'
test_classifer.py: dir = '/opt/pynpf-data'

http://seprojects.marum.de:8888/?token=02c6cbada19ebb4f1dbd7e9de197d9e63c5dd62276664d09
http://seprojects.marum.de:8888/notebooks/example.ipynb


