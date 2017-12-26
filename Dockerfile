FROM jupyterhub/jupyterhub:latest
COPY jupyterhub_config.py /srv/jupyterhub/
RUN conda install notebook
RUN conda install pandas
RUN conda install requests
RUN conda install matplotlib
RUN conda install basemap
RUN conda install scipy
RUN conda install -c conda-forge ipywidgets
RUN pip install rdflib
RUN pip install sklearn
RUN pip install geomet
RUN pip install ipyleaflet
RUN jupyter nbextension enable --py --sys-prefix ipyleaflet
RUN adduser -q --gecos "" --disabled-password npf
RUN echo npf:npf | chpasswd
RUN git clone https://github.com/markusstocker/pynpf.git /home/npf/pynpf
RUN chown -R npf.npf /home/npf/pynpf
RUN openssl req -x509 -newkey rsa:1024 -keyout /srv/jupyterhub/jhub.key -out /srv/jupyterhub/jhub.crt -days 365 -nodes -subj "/C=DE/ST=./L=./O=./OU=./CN=."
