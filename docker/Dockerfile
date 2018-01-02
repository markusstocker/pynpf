FROM jupyterhub/jupyterhub:latest
COPY jupyterhub_config.py /srv/jupyterhub/
RUN conda install -c conda-forge conda-build notebook pandas requests matplotlib basemap scipy ipywidgets
RUN conda update -n root conda-build
RUN pip install rdflib sklearn geomet ipyleaflet
RUN jupyter nbextension enable --py --sys-prefix ipyleaflet
RUN openssl req -x509 -newkey rsa:1024 -keyout /srv/jupyterhub/jhub.key -out /srv/jupyterhub/jhub.crt -days 365 -nodes -subj "/C=DE/ST=./L=./O=./OU=./CN=."
RUN adduser -q --gecos "" --disabled-password npf
RUN echo npf:npf | chpasswd
RUN git clone https://github.com/markusstocker/pynpf.git /tmp/pynpf
WORKDIR /tmp/pynpf
RUN conda build conda.recipe
RUN conda install --use-local pynpf
RUN git clone https://github.com/markusstocker/pynpf-notebooks.git /tmp/pynpf-notebooks
WORKDIR /tmp/pynpf-notebooks
RUN cp *.ipynb /home/npf
RUN chown -R npf.npf /home/npf/*.ipynb
WORKDIR /srv/jupyterhub/