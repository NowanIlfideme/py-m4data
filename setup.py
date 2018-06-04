"""Setup file for packaging."""

from os import path
from codecs import open as copen # To use a consistent encoding
from setuptools import setup, find_packages

description = "Dataset for the M4 (Makridakis-4) time series competition"
here = path.abspath(path.dirname(__file__))
try:
    with copen(path.join(here, 'readme.rst'), encoding='utf-8') as f:
        long_description = f.read()
except: long_description = description


version_dict = {}
with copen(path.join(here,"wpm_utilization/version.py")) as fp:
    exec(fp.read(), version_dict)
version = version_dict['version']

setup(name="m4data",
    version = package_version,
    description = description,
    long_description = long_description,
    author = "Anatoly Makarevich",
    author_email = "anatoly_mak@yahoo.com",
    url = "https://github.com/NowanIlfideme/py-m4data",
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',

        # unsure about this one - couldn't find M4 lisence terms
        # and unsure whether you can re-lisence, so I'll keep this commented for now
        #'License :: Public Domain', 
        ],
    packages = find_packages(),
    install_requires = [
        "pandas",
        ],
    #entry_points = {'console_scripts': ['full_run=full_run',],} # Not used currently
    )


