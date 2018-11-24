# -*- coding: utf-8 -*-
from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


# read package description
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# read package requirements
with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='pybootstrap',
    version='0.1.0',
    description='Bootstrap Python package',
    long_description=long_description,
    url='http://github.com/sebastianlach/pybootstrap',
    author='Sebastian Łach',
    author_email='root@slach.eu',
    license='GNU',
    packages=['pybootstrap'],
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True,
)
