"""setup.py file."""

import uuid

from setuptools import setup, find_packages

__author__ = 'David Barroso <dbarrosop@dravetech.com>'

setup(
    name="napalm-fortios",
    version="0.4.1",
    packages=find_packages(),
    author="David Barroso",
    author_email="dbarrosop@dravetech.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm-fortios",
    include_package_data=True,
    install_requires=[
        'napalm',
        'future',
        'ncclient==0.6.15',
        'pyfg @ git+https://gitlab-ce.gwdg.de/gwdg-netz/pyfg.git#egg=pyfg',
    ],
)
