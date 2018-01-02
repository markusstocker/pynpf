from setuptools import setup, find_packages
import os.path as op
import sys

install_requires = [
    'matplotlib',
    'pandas',
    'requests',
    'basemap',
    'scipy',
    'rdflib',
    'geomet',
    'sklearn',
    'ipyleaflet'
]

setup(
    name='pynpf',
    version='0.1',
    description='A package with specialized functions to perform particle formation analysis',
    url='https://github.com/markusstocker/pynpf',
    author='Markus Stocker',
    author_email='markus.stocker@gmail.com',
    license='GPL',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(),
    package_data={'pynpf': ['query/resources/*.rq', 'learning/models/*.pkl']},
    include_package_data=True,
    entry_points={},
    install_requires=install_requires,
)
